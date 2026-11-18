# ATTENTION!! DEPRECATED!!!!!!
from .. gl_fun import bat, DrawBlend, Bind
from .. gpu_sh import Shader2D, ShaderType


img_shader = Shader2D.IMAGE()
tex_coord = ((0, 0), (1, 0), (1, 1), (0, 1))
def verts(p, s):
    x, y = p
    w, h = s
    return ((x,y),(x+w,y),(x+w,y+h),(x,y+h))


def Draw_Image(_p, _s, _i, shader=img_shader):
    b = bat(shader, ShaderType.TRIFAN(), {'pos':verts(_p, _s), 'texCoord':tex_coord})
    # bgl was removed in Blender 5.0: _i must be a gpu.types.GPUTexture.
    shader.bind()
    shader.uniform_sampler("image", _i)
    DrawBlend(b, shader)
