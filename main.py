import sys,os,time
import pygame
from pygame.locals import *
from sys import exit
#paths
audios_path=os.path.join(os.path.dirname(__file__),"audios")
images_path=os.path.join(os.path.dirname(__file__),"images")
#images
os.chdir(images_path)
icon=pygame.image.load(os.path.join("icon","icon.ico"))
bg_start=pygame.image.load(os.path.join("bg","bg_start.png"))#760x650
bg_game=pygame.image.load(os.path.join("bg","bg_game.png"))
button_start0=pygame.image.load(os.path.join("buttons","startgame_0.png"))#95x45
button_start1=pygame.image.load(os.path.join("buttons","startgame_1.png"))
sign=pygame.image.load(os.path.join("chessman","sign.png"))#30x30
chessman_black=pygame.image.load(os.path.join("chessman","black.png"))#30x30
chessman_white=pygame.image.load(os.path.join("chessman","white.png"))#30x30
#pygame init
pygame.init()
screen=pygame.display.set_mode((760,650))
pygame.display.set_caption("五子棋")
pygame.display.set_icon(icon)
#colors
color_black=(0,0,0)
color_red=(255,0,0)
#constants
start_button_rect=(75,450,95,45)#start_x,start_y,size_x,size_y
block_info=(34,35,30,30)#start_x,start_y,size_x,size_y
#variables(global)
map=[[-1]*19 for i in range(19)]#-1:empty 0:black 1:white
#utilities
def inrect(spot,rect):
    return spot[0]>rect[0] and spot[1]>rect[1] and \
    spot[0]<rect[0]+rect[2] and spot[1]<rect[1]+rect[3]
def rpos2pos(rpos):
    return ((rpos[0]-block_info[0])//block_info[2],\
            (rpos[1]-block_info[1])//block_info[3])
def pos2rpos(pos):
    return (block_info[0]+pos[0]*block_info[2],\
            block_info[1]+pos[1]*block_info[3])
#functions
def start():
    while 1:
        #display
        screen.blit(bg_start,(0,0))
        #event
        mousedown=0
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type==MOUSEBUTTONDOWN:
                mousedown=1
        spot=pygame.mouse.get_pos()
        if inrect(spot,start_button_rect):
            screen.blit(button_start1,start_button_rect[0:2])
            if mousedown:
                break
        else:
            screen.blit(button_start0,start_button_rect[0:2])
        #update
        pygame.display.update()

def main():#unfinished
    show_lines=False
    mode=0#0:black 1:white
    while 1:
        #display
        screen.blit(bg_game,(0,0))
        if show_lines:
            for i in range(20):
                pygame.draw.line(screen,color_red,pos2rpos((i,0)),pos2rpos((i,19)),1)
            for i in range(20):
                pygame.draw.line(screen,color_red,pos2rpos((0,i)),pos2rpos((19,i)),1)
        for i in range(19):
            for j in range(19):
                if map[i][j]==0:
                    screen.blit(chessman_black,pos2rpos((i,j)))
                elif map[i][j]==1:
                    screen.blit(chessman_white,pos2rpos((i,j)))
        #event
        mousedown=0
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    mousedown=1
                elif event.button==3:
                    show_lines=not show_lines
        rpos=pygame.mouse.get_pos()
        pos=rpos2pos(rpos)
        if inrect(pos,(-1,-1,20,20)) and map[pos[0]][pos[1]]==-1:
            print(pos)
            screen.blit(sign,pos2rpos(pos))
            if mousedown:
                if mode:
                    map[pos[0]][pos[1]]=1
                else:
                    map[pos[0]][pos[1]]=0
                mode=not mode
        #update
        pygame.display.update()
    

start()
main()

pygame.quit()