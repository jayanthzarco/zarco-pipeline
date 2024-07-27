import sys

import maya.cmds as cmds
import os
# sys.path.append(os.path.abspath(__file__))
sys.path.append('E:/Git___/zarco-pipeline')

class ZarcoMenuBar:
    def __init__(self):
        if cmds.menu('_zarco_menu', exists=True):
            cmds.deleteUI('_zarco_menu', menu=True)
        self.menu = None
        self.zarco_menubar()

    def zarco_menubar(self):
        self.menu = cmds.menu('_zarco_menu_', label='zarco_menu', parent='MayaWindow', tearOff=True)

        # Adding main categories
        self.add_modeling_menu()
        self.add_texturing_menu()
        self.add_rigging_menu()
        self.add_animation_menu()
        self.add_lighting_menu()
        self.add_rendering_menu()

    def add_modeling_menu(self):
        modeling_menu = cmds.menuItem(label='Modeling', subMenu=True, parent=self.menu, tearOff=True)

    def add_texturing_menu(self):
        texturing_menu = cmds.menuItem(label='Texturing', subMenu=True, parent=self.menu, tearOff=True)

    def add_rigging_menu(self):
        rigging_menu = cmds.menuItem(label='Rigging', subMenu=True, parent=self.menu, tearOff=True)
        cmds.menuItem(label='Auto_Rig', parent=rigging_menu, command=lambda *args: self._auto_rig())
        cmds.menuItem(label='JZ_Renamer', parent=rigging_menu, command=lambda *args: self._jz_renamer())
        cmds.menuItem(label='Scene_Optimizer', parent=rigging_menu, command=lambda *args: self._scene_optimizer())
        cmds.menuItem(label='Duplicate_Node_Renamer', parent=rigging_menu,
                      command=lambda *args: self._duplicate_node_renamer())

    def add_animation_menu(self):
        animation_menu = cmds.menuItem(label='Animation', subMenu=True, parent=self.menu, tearOff=True)


    def add_lighting_menu(self):
        lighting_menu = cmds.menuItem(label='Lighting', subMenu=True, parent=self.menu, tearOff=True)

    def add_rendering_menu(self):
        rendering_menu = cmds.menuItem(label='Rendering', subMenu=True, parent=self.menu, tearOff=True)
        cmds.menuItem(label='Quick_Renderer', parent=rendering_menu, command=lambda *args: self._quick_renderer())

    @staticmethod
    def _auto_rig():
        from packages.maya.AUTORIG import maya_call
        print("calling Auto Rig")
        maya_call.run()

    @staticmethod
    def _jz_renamer():
        print("calling JZ_Renamer")

    @staticmethod
    def _scene_optimizer():
        print("calling Scene Optimizer")

    @staticmethod
    def _quick_renderer():
        print("calling Quick Renderer")

    @staticmethod
    def _duplicate_node_renamer():
        print("calling Duplicate Node Renamer")


if __name__ == '__main__':
    _run = ZarcoMenuBar()
