from GUI import GUI
from interface_objects import Patch, ShakingPatch, Label, Button


def init_interface(gui_object):
    patch1 = ShakingPatch((20, 20), (50, 50))
    patch2 = Patch((100, 20), (70, 90), (0, 0, 255))

    gui_object.add_element(patch1)
    gui_object.add_element(patch2)

    gui_object.add_element(Label((100, 100), (0, 0), "Hello world"))


    def stop():
        gui._is_running = False

    gui_object.add_element(Button(stop, (200, 200), (150, 50)))


    def move_patch():
        patch2.position = (patch2.position[0] + 10, patch2.position[1])


    gui_object.add_element(Button(move_patch, (200, 300), (150, 50), (0, 0, 255)))


if __name__ == "__main__":
    gui = GUI()

    init_interface(gui)

    gui.run()
