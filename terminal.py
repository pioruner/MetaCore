from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings

buffer1 = Buffer()
kb = KeyBindings()


@kb.add('c-q')
def exit_(event):
    event.app.exit()


def terminal_run_ui():
    root_container = VSplit([
        Window(content=BufferControl(buffer=buffer1), width=20),
        Window(width=1, char='|'),
     Window(content=FormattedTextControl(text='Hello world')),
    ])
    layout = Layout(root_container)
    app = Application(key_bindings=kb, layout=layout, full_screen=True)
    app.run()
