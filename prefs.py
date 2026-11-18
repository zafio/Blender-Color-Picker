from bpy.types import AddonPreferences
from bpy.props import StringProperty, FloatProperty, FloatVectorProperty, BoolProperty, BoolVectorProperty, EnumProperty, IntVectorProperty, IntProperty
from . data import copktype
from . km import get_keyitem, get_keyitem_mode, modes
panel_layout = "lay" + "out"
SUPPORT_URL = "https://superhivemarket.com/products/color-picker"


def get_prefs(context):
    return context.preferences.addons[__package__].preferences


class ColorPickerPreferences(AddonPreferences):
    bl_idname = __package__

    close_on_hotkey_release: BoolProperty(
        default=True, name="Close on Hot-key Release")

    is_dirty: BoolProperty(default=False)

    color_picker_type: EnumProperty(
        items=copktype,
        default='SV_RECT',
        name="Color Picker Type"
    )
    color_picker_use_slice: BoolProperty(
        default=False, name="Slice Color Picker")

    scale: FloatProperty(name="Scale Factor", min=0.5, max=2, default=1,
                         description="Size multiplier for the picker, on top of the Screen DPI")

    screen_dpi: IntProperty(default=72, min=72, max=300, name="Screen DPI",
                            description="The greater this value is, the greater the size of the text and widget will be :-)")
    #slices : FloatVectorProperty(size=4, min=0, max=1, default=(0, 1, 0, 1))
    show_hex: BoolProperty(default=False, name="Show Hex",
                           description="Show hexadecimal color code")

    def draw(self, context):
        scn = context.scene
        layout = getattr(self,  panel_layout)
        layout.use_property_split = True
        layout.use_property_decorate = False

        #teg_data = scn.color_picker_teg
        #color_picker = teg_data.color_picker

        if isinstance(self, AddonPreferences):
            fund = layout.box()
            fund.label(text="Support the Development", icon='FUND')
            col = fund.column(align=True)
            col.label(text="Thanks to your support, Color Picker stays open, free and public.")
            col.label(text="If it saves you time, consider buying it on Superhive.")
            row = fund.row()
            row.scale_y = 1.6
            row.operator('wm.url_open', text="Development Fund ♥", icon='FUND').url = SUPPORT_URL
            layout.separator()

        settings = layout.column(align=True)
        header = settings.box()
        header.label(text="Settings :", icon='SETTINGS')

        props = settings.box()

        if not isinstance(self, AddonPreferences):
            self = get_prefs(context)

            # props.prop(self, 'texture_size_factor' if context.mode == 'PAINT_TEXTURE' else 'weight_size_factor' if context.mode ==
            #            'PAINT_WEIGHT' else 'vertex_size_factor', slider=True)
            if context.mode != 'PAINT_WEIGHT':
                props.prop(self, 'color_picker_type')

            kmi = get_keyitem(context)
            if kmi:
                box = settings.box()
                box.label(text="Keymap :")
                row = box.row()
                row.label(text="Press Key")
                row.template_event_from_keymap_item(kmi)
                row = box.row(align=True)
                row.prop(kmi, 'map_type', text="")
                row.prop(kmi, 'type', text="")

                row = box.row()
                row.use_property_split = False
                row.prop(self, 'close_on_hotkey_release')

        else:
            props.prop(self, 'scale', slider=True)
           # props.prop(self, 'texture_size_factor', slider=True)
           # props.prop(self, 'weight_size_factor', slider=True)
           # props.prop(self, 'vertex_size_factor', slider=True)

            props.prop(self, 'color_picker_type')

            box = settings.box()
            box.label(text="Keymap :")

            for mode in modes:
                kmi = get_keyitem_mode(context, mode)
                if kmi:
                    row = box.row()
                    row.label(text=mode)
                    row.template_event_from_keymap_item(kmi)
                    row = box.row(align=True)
                    row.prop(kmi, 'map_type', text="")
                    row.prop(kmi, 'type', text="")
            box.separator()
            row = box.row()
            row.use_property_split = False
            row.prop(self, 'close_on_hotkey_release')

        props.prop(self, 'screen_dpi', text="Screen DPI")
        props.prop(self, 'show_hex')
