from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *


def myInit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1, 1, 1, 1)  # clear background
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60, 1, 0.1, 50)
    gluLookAt(10, 10, 10, 0, 0, 0, 0, 1, 0)

def chair():
    #legs
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0.75, 0.9, 0.75)
    glTranslate(3, -2, -1.5)
    glScale(0.5, 3, 0.5)
    glutSolidCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0.75, 0.9, 0.75)
    glTranslate(-3, -4, -3)
    glScale(0.5, 4, 0.5)
    glutSolidCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0.75, 0.9, 0.75)
    glTranslate(-2, -3, 2.1)
    glScale(0.5, 3, 0.5)
    glutSolidCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0.75, 0.9, 0.75)
    glTranslate(2.7, -2.5, 2.3)
    glScale(0.5, 2.8, 0.5)
    glutSolidCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()  # set
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0.75, 0.9, 0.75)
    glScale(2.9, 0.5, 2.5)
    glutSolidCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()  # back
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0.75, 0.9, 0.75)
    glTranslate(0, 2.5, -3)
    glScale(3, 2.6, 0.5)
    glutSolidCube(2)
    glPopAttrib()
    glPopMatrix()


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    chair()                #draw first chair
    glTranslate(-9, 0, 0) # draw second chair
    chair()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Two_Chairs")
glutDisplayFunc(draw)
glutIdleFunc(draw)
myInit()
glutMainLoop()