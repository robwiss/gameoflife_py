import purepy_engine as engine
import pyglet
 
def pyglet_way():
    x, y = 200, 100

    grid = engine.grid.Grid(x, y)
    engine.randomize(grid)

    scale = 4
    x *= scale
    y *= scale
    red = 1.0, 0, 0, 1.0
    gray20 = 0.2, 0.2, 0.2, 1.0
    whitesmoke = 0.9607, 0.9607, 0.9607, 1.0
    lightsalmon = 1.0, 0.6275, 0.4784, 1.0

    window = pyglet.window.Window(width=x, height=y)
    pyglet.gl.glClearColor(*gray20)
    pyglet.gl.glColor4f(*lightsalmon)

    gl_flag, indices = 'v2i', (0, 1, 2, 0, 2, 3)

    def draw_square(point, size):
        x, y = point[0] * size, point[1] * size
        x_size, y_size = x+size, y+size
        vertices = x,y, x_size,y, x_size,y_size, x,y_size
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, indices, (gl_flag, vertices))

    def process_living(changes):
        for point, value in changes:
            if value == True:
                draw_square(point, scale)

    def on_draw(self):
        #callback needs self
        window.clear()
        go()


    def go():
        changes = engine.tick(grid)
        process_living(changes)

    pyglet.clock.schedule(on_draw)
    pyglet.app.run()
 
if __name__ == "__main__":
    pyglet_way()
