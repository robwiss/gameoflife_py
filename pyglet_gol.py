import engine
import pyglet
 
def pyglet_way():
    rows, cols = 100, 100

    cells = engine.randomized_cells((rows,cols))

    scale = 4
    red = 1.0, 0, 0, 1.0
    colors = {
        'red'         : (1.0,    0,      0,      1.0),
        'gray20'      : (0.2,    0.2,    0.2,    1.0),
        'whitesmoke'  : (0.9607, 0.9607, 0.9607, 1.0),
        'lightsalmon' : (1.0,    0.6275, 0.4784, 1.0)
    }

    window = pyglet.window.Window(width=cols*scale, height=rows*scale)
    pyglet.gl.glClearColor(*colors['gray20'])
    pyglet.gl.glColor4f(*colors['whitesmoke'])

    gl_flag, indices = 'v2i', (0, 1, 2, 0, 2, 3)

    def draw_square(point, size):
        x, y = point[1] * size, (rows - point[0]) * size
        x_size, y_size = x+size, y+size
        vertices = x,y, x_size,y, x_size,y_size, x,y_size
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, indices, (gl_flag, vertices))

    def process_living(cells):
        for point in cells:
            draw_square(point, scale)

    def on_draw(self):
        #callback needs self
        window.clear()
        process_living(cells)
        engine.tick(cells)

    pyglet.clock.schedule(on_draw)
    pyglet.app.run()
 
if __name__ == "__main__":
    pyglet_way()
