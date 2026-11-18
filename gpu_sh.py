from gpu.shader import from_builtin#, code_from_builtin # NOTE: Exposes the internal shader code for query.
import re
import gpu


# Blender 5.0 removed the legacy `GPUShader(vertexcode, fragcode)` constructor.
# This adapter keeps the original GLSL sources (with `uniform`/`in`/`out`
# declarations) and converts them into a `GPUShaderCreateInfo` based shader.
_GLSL_TYPES = {
    'float': 'FLOAT', 'int': 'INT', 'bool': 'BOOL', 'uint': 'UINT',
    'vec2': 'VEC2', 'vec3': 'VEC3', 'vec4': 'VEC4',
    'ivec2': 'IVEC2', 'ivec3': 'IVEC3', 'ivec4': 'IVEC4',
    'mat3': 'MAT3', 'mat4': 'MAT4',
}
_DECL_RE = re.compile(r'^[ \t]*(uniform|in|out)[ \t]+(\w+)[ \t]+(\w+)[ \t]*;[ \t]*$', re.M)


def _extract(code: str):
    decls = [(m.group(1), m.group(2), m.group(3)) for m in _DECL_RE.finditer(code)]
    return decls, _DECL_RE.sub('', code)


def Shader(vertexcode: str, fragcode: str, libcode: str = None, name: str = 'ColorPicker'):
    vs_decls, vs_src = _extract(vertexcode)
    fs_decls, fs_src = _extract(fragcode)
    if libcode:
        fs_src = libcode + '\n' + fs_src

    info = gpu.types.GPUShaderCreateInfo()
    iface = None
    added_uniforms = set()
    sampler_slot = 0
    vert_in_slot = 0
    frag_out_slot = 0
    push_constants = []

    def add_uniform(t, n):
        nonlocal sampler_slot
        if n in added_uniforms:
            return
        added_uniforms.add(n)
        if t == 'sampler2D':
            info.sampler(sampler_slot, 'FLOAT_2D', n)
            sampler_slot += 1
        else:
            push_constants.append((t, n))

    for q, t, n in vs_decls:
        if q == 'uniform':
            add_uniform(t, n)
        elif q == 'in':
            info.vertex_in(vert_in_slot, _GLSL_TYPES[t], n)
            vert_in_slot += 1
        elif q == 'out':
            if iface is None:
                iface = gpu.types.GPUStageInterfaceInfo(name + '_iface')
            iface.smooth(_GLSL_TYPES[t], n)
    for q, t, n in fs_decls:
        if q == 'uniform':
            add_uniform(t, n)
        elif q == 'out':
            info.fragment_out(frag_out_slot, _GLSL_TYPES[t], n)
            frag_out_slot += 1
        # 'in' variables come from the stage interface declared by the VS.
    # Largest first to avoid std140-like padding (128 bytes push-constant budget).
    _size = {'mat4': 64, 'mat3': 48, 'vec4': 16, 'ivec4': 16, 'vec3': 12, 'ivec3': 12, 'vec2': 8, 'ivec2': 8}
    for t, n in sorted(push_constants, key=lambda tn: -_size.get(tn[0], 4)):
        info.push_constant(_GLSL_TYPES[t], n)
    if iface is not None:
        info.vertex_out(iface)
    info.vertex_source(vs_src)
    info.fragment_source(fs_src)
    return gpu.shader.create_from_info(info)
from . libcode import *
from enum import Enum


class ShaderName2D(Enum):
    IMAGE   = 'IMAGE'
    UNIFORM = 'UNIFORM_COLOR'
    FLAT    = 'FLAT_COLOR'
    SMOOTH  = 'SMOOTH_COLOR'

    def __call__(self):
        return self.value

'''
NOTE:
Shaders that are embedded in the blender internal code.
They all read the uniform ‘mat4 ModelViewProjectionMatrix’, which can be edited by the ‘gpu.matrix’ module.
For more details, you can check the shader code with the function ‘gpu.shader.code_from_builtin’.

https://docs.blender.org/api/blender2.8/gpu.shader.html?highlight=builtin#gpu.shader.code_from_builtin

'''
# Shader References:
# https://docs.blender.org/api/blender2.8/gpu.html#d-image
# https://docs.blender.org/api/blender2.8/gpu.html#d-rectangle
# https://github.com/lewislepton/shadertutorialseries
# https://github.com/dfelinto/blender/tree/master/source/blender/gpu/shaders
# https://medium.com/@pythor/cool-shaders-f071a491245
shader_2d_image         = from_builtin(ShaderName2D.IMAGE())
shader_2d_color_unif    = from_builtin(ShaderName2D.UNIFORM())
shader_2d_color_flat    = from_builtin(ShaderName2D.FLAT())
shader_2d_color_smooth  = from_builtin(ShaderName2D.SMOOTH())

class Shader2D(Enum):
    IMAGE   = shader_2d_image
    UNIFORM = shader_2d_color_unif
    FLAT    = shader_2d_color_flat
    SMOOTH  = shader_2d_color_smooth

    def __call__(self):
        return self.value

class ShaderName3D(Enum):
    UNIFORM = 'UNIFORM_COLOR'
    FLAT    = 'FLAT_COLOR'
    SMOOTH  = 'SMOOTH_COLOR'

    def __call__(self):
        return self.value
from .__lib__ import *
shader_3d_color_unif    = from_builtin(ShaderName3D.UNIFORM())
shader_3d_color_flat    = from_builtin(ShaderName3D.FLAT())
shader_3d_color_smooth  = from_builtin(ShaderName3D.SMOOTH())

class Shader3D(Enum):
    UNIFORM = shader_3d_color_unif
    FLAT    = shader_3d_color_flat
    SMOOTH  = shader_3d_color_smooth

    def __call__(self):
        return self.value

class ShaderType(Enum):
    POINTS      = "POINTS"
    LINES       = "LINES"
    TRIS        = "TRIS"
    LINES_ADJ   = "LINES_ADJ"
    TRIFAN      = "TRI_FAN"

    def __call__(self):
        return self.value

def ShaderLib(shc, lib):
    return Shader(*shc, libcode=lib)

# TODO: Make it beautiful, PLEASE...
class SH(Enum):
    # PLIGHT = Shader(*SHCx504C49474854)
    # CFS_CROPTOP = Shader(*SHCx4346535F43524F50544F50)
    # CFS_CROPBOT = Shader(*SHCx4346535F43524F50424F54)
    IMGA = Shader(*SHCx494D4741) # see image.py for reference.
    IMGA_GAMMA = Shader(*SHCx494D47415F47414D434F) # same as above but with some pow for gamma correcting.
    IMGA_GAMMA_INTENSIFY = Shader(*SHCx494D47415F47414D434F5F424F4F5354) # same as above but multiplied values to make it brighter.
    # RNGS_SPLITANG = Shader(*SHCx524E47535F53504C4954414E47)
    # RNGBLR = Shader(*SHCx524E47424C52)
    IMGA_GAMMA_OP = Shader(*SHCx494D47415F47414D4D415F4F50) # same as IMGA_GAMMA but multiplied alpha.
    # IMGA_LINE = Shader(*SHCx494D47415F4C494E45)
    BARCROMA_H = Shader(*SHCx42415243524f4d415f48)
    RCROMA_SL = Shader(*SHCx4343524F4D415F534C)
    RCROMA_SL_LIN = Shader(*SHCx5243524f4d415f534c5f4c494e)
    CCROMA_HS = Shader(*SHCx4343524F4D415F4853)
    BARCROMA_V = Shader(*SHCx42415243524f4d415f56)
    BARCROMA_G = Shader(*SHCx42415243524f4d415f47)
    CRCROMA_H = Shader(*SHCx4343524F4D415F48)
    CFS = Shader(*SHCx434653)
    BARCROMA_S = Shader(*SHCx42415243524f4d415f53)
    BARCROMA_R = Shader(*SHCx42415243524f4d415f52)
    RCROMA_SL_NOLIN = Shader(*SHCx5243524f4d415f534c5f4e4f4c494e)
    RCTGRAD_LIN = Shader(*SHCx524354475241445f4c494e)
    RCTGRAD_NOLIN = Shader(*SHCx524354475241445f4e4f4c494e)
    RCTGRADBAR_LIN = Shader(*SHCx524354475241445f4e4f4c494e10)
    RCTGRADBAR_NOLIN = Shader(*SHCx524354475241445f4e4f4c494e11)
    RCROMA_SL_LIN_SLICE = Shader(*SHCx5243524f4d41534c4c494e534c494345)
    RCTDOT_MASK = Shader(*SHCx524354444f545f4d41534b)
    BARCROMA_B = Shader(*SHCx42415243524f4d415f42)
    
    def __call__(self):
        return self.value
