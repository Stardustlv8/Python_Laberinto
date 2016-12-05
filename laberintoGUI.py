"""algoritmo de busqueda primero a lo profundo"""

laberinto = "##################\n" + \
            "##.##...#...#...##\n" + \
            "#...#.#.#.#.#.#.##\n" + \
            "#.#.#.#...#...#.##\n" + \
            "#.#.#.#####.###.##\n" + \
            "#.#.#.###.#.##...#\n" + \
            "#.###...#...#..#.#\n" + \
            "#.#####.########.#\n" + \
            "#...........#....#\n" + \
            "###########.#.####"

laberinto1= "###########\n" + \
            "#.........#\n" + \
            "#.###.#.#.#\n" + \
            "#...#.#.#.#\n" + \
            "###.#####.#\n" + \
            "#...#.....#\n" + \
            "###.#.#####"

"""inicial = (9,11,)
lab = crea_laberinto(laberinto)
#visitados = search_DFS(inicial, laberinto)
visitados = search_BFS(inicial, laberinto)

run_lab(visitados,lab)
for x in visitados:
    print x
"""
from BFS import search_BFS
from Split import impLab, crea_laberinto
from run_laberinto import run_lab
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

inicial = (9,11,)
lab = crea_laberinto(laberinto)
#visitados = search_DFS(inicial, laberinto)
visitados = search_BFS(inicial, laberinto)

class Handler:
    def on_window1_delete_event(self, *args):
        Gtk.main_quit(*args)

    def on_imagemenuitem5_button_press_event(self, *args):
        Gtk.main_quit(*args)

    def on_textview4_key_press_event(self, *args):
	texto.get_buffer().set_text(laberinto)


builder = Gtk.Builder()
builder.add_from_file("LaberintoGUI.glade")
builder.connect_signals(Handler())
window = builder.get_object("window1")
texto = builder.get_object("textview4")
window.show_all()
Gtk.main()
