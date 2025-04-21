import os, json, math
import pygame

def read_json(path):
    f = open(path, 'r')
    dat = f.read()
    f.close()
    return json.loads(dat)

def get_dis(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def load_rags(path):
    rag_list = os.listdir(path)
    rags = {}
    for rag in rag_list:
        rags[rag.split('.')[0]] = read_json(path + '/' + rag)
    return rags

class ImageClothObj():
    def __init__(self, surface = pygame.surface.Surface, scale = int):
        self.shading = False
        self.timercount = 0
        self.surface = pygame.surface.Surface((surface.get_width() + 0, surface.get_height() + 0)).convert_alpha()
        self.surface.blit(surface.convert_alpha(),(0,0))
        self.surface.set_colorkey(pygame.color.Color(0,0,0))
        
        self.grounded = []
        self.points = []

        x, y = surface.get_size()
        
        
        x = int(x)
        y = int(y)

        for row in range(y):
            for col in range(x):
                try:
                        #self.grounded.append(row * surface.get_width() + col)
                    #if surface.get_at((col, row)) != (0, 0, 0, 0):
                        if row in [0]:
                                if col in [0,1,2, x-1,x-2,x-3]:
                                    self.grounded.append(row * surface.get_width() + col)
                        self.points.append([col, row, col, row])
                except:
                    pass
        self.orig_points = [p + p for p in self.points]
        self.scale = scale
        self.sticks = []
        for row in range(y):
            for col in range(x + 1):
                #if surface.get_at((col, row)) != (0, 0, 0, 0):
                    if col == x-1:
                        try:
                            pass
                            #self.add_stick([row * surface.get_width() + col, row * surface.get_width() + col])
                        except:
                            pass
                        try:
                            pass
                        except:
                            pass
                    try:
                        if col + 1 != x:
                            #HORIZONTAL STICKS
                            self.add_stick([row * surface.get_width() + col, row * surface.get_width() + col + 1])
                        #if surface.get_at((col, row + 1)) != (0, 0, 0, 0):
                        #VERTICAL STICKS
                        self.add_stick([row * surface.get_width() + col, (row + 1) * surface.get_width() + col])
                    except:
                        pass
    
    def add_stick(self, points):
        self.sticks.append([points[0], points[1], get_dis(self.points[points[0]][:2], self.points[points[1]][:2])])

    def update(self, externalForce = [0, 0]):
        
        for i, point in enumerate(self.points):
            if i not in self.grounded:
                d_x = point[0] - point[2]
                d_y = point[1] - point[3]
                point[2] = point[0]
                point[3] = point[1]
                point[0] += d_x
                point[1] += d_y
                point[1] += 0.05 + externalForce[1] / self.scale
                point[0] += externalForce[0] / self.scale
    
    def move_grounded(self, offset):
        for i, point in enumerate(self.points):
            if i in self.grounded:
                point[0] = self.orig_points[i][0] + offset[0] / self.scale
                point[1] = self.orig_points[i][1] + offset[1] / self.scale
                point[2] = point[0]
                point[3] = point[1]

    def update_sticks(self):
        for stick in self.sticks:
            dis = get_dis(self.points[stick[0]][:2], self.points[stick[1]][:2])
            dis_dif = stick[2] - dis
            mv_ratio = dis_dif / dis / 2
            dx = self.points[stick[1]][0] - self.points[stick[0]][0]
            dy = self.points[stick[1]][1] - self.points[stick[0]][1]
            mult = 0.95
            if stick[0] not in self.grounded:
                self.points[stick[0]][0] -= dx * mv_ratio * mult
                self.points[stick[0]][1] -= dy * mv_ratio * mult
            if stick[1] not in self.grounded:
                self.points[stick[1]][0] += dx * mv_ratio * mult
                self.points[stick[1]][1] += dy * mv_ratio * mult

    '''def render_polygon(self, target_surf, color, offset=[0, 0]):
        y_points = [p[1] * self.scale for p in self.points]
        x_points = [p[0] * self.scale for p in self.points]
        min_x = min(x_points)
        max_x = max(x_points)
        min_y = min(y_points)
        max_y = max(y_points)
        width = int(max_x - min_x + 2)
        height = int(max_y - min_y + 2)
        surf = pygame.Surface((width, height))
        self.render_sticks(surf, (int(min_x), int(min_y)))
        surf.set_colorkey((0, 0, 0))
        m = pygame.mask.from_surface(surf)
        outline = m.outline() # get outline of mask
        surf.fill((0, 0, 0)) # fill with color that will be colorkey
        surf.set_colorkey((0, 0, 0))
        pygame.draw.polygon(surf, self.surface.get_at(offset), outline)
        target_surf.blit(surf, (min_x - offset[0], min_y - offset[1]))'''
    
    def render_texture(self, target_surf, color, offset=[0, 0]):
        
        render_points = [[p[0] * self.scale - offset[0], p[1] * self.scale - offset[1]] for p in self.points]
        for row in range(self.surface.get_height()):
            for col in range(self.surface.get_width()):
                if col + 1 != self.surface.get_width():
                    
                    try:
                        vector1 = pygame.Vector2((render_points[row * self.surface.get_width() + col])[0],(render_points[row * self.surface.get_width() + col])[1])
                        vector2 = pygame.Vector2((render_points[(row + 1) * self.surface.get_width() + col+1])[0],(render_points[(row + 1) * self.surface.get_width() + col+1])[1])
                        colorsub = self.surface.get_at((col, row))
                        colormult = 25
                        if self.shading:
                            colorsub = pygame.color.Color( min(254,max(1,int(colorsub[0] - (vector1.distance_to(vector2) * colormult)/self.scale))),
                                                          min(254,max(1,int(colorsub[1] - (vector1.distance_to(vector2) * colormult)/self.scale))),
                                                          min(254,max(1,int(colorsub[2] - (vector1.distance_to(vector2) * colormult)/self.scale))))

                        pygame.draw.polygon(target_surf, colorsub, [render_points[row * self.surface.get_width() + col],
                                                                                        render_points[(row + 1) * self.surface.get_width() + col],
                                                                                        render_points[(row + 1) * self.surface.get_width() + col+1],
                                                                                        render_points[row * self.surface.get_width() + col+1],], 0)
                    except:
                        pass
        if pygame.mouse.get_pressed()[0] == True:
            self.render_sticks(target_surf, offset)
        

    def render_sticks(self, surf, offset=[0, 0]):
        render_points = [[p[0] * self.scale - offset[0], p[1] * self.scale - offset[1]] for p in self.points]
        for stick in self.sticks:
            pygame.draw.line(surf, (0, 0, 0), render_points[stick[0]], render_points[stick[1]], 1)

class ClothObj():
    def __init__(self, rag):
        self.points = [p + p for p in rag['points']] # dupe position for last position
        self.orig_points = [p + p for p in rag['points']]
        self.sticks = []
        self.scale = rag['scale']
        for stick in rag['connections']:
            self.add_stick(stick)
        self.grounded = rag['grounded']

    def add_stick(self, points):
        self.sticks.append([points[0], points[1], get_dis(self.points[points[0]][:2], self.points[points[1]][:2])])

    def update(self):
        for i, point in enumerate(self.points):
            if i not in self.grounded:
                d_x = point[0] - point[2]
                d_y = point[1] - point[3]
                point[2] = point[0]
                point[3] = point[1]
                point[0] += d_x
                point[1] += d_y
                point[1] += 0.05

    def move_grounded(self, offset):
        for i, point in enumerate(self.points):
            if i in self.grounded:
                point[0] = self.orig_points[i][0] + offset[0] / self.scale
                point[1] = self.orig_points[i][1] + offset[1] / self.scale
                point[2] = point[0]
                point[3] = point[1]

    def update_sticks(self):
        for stick in self.sticks:
            dis = get_dis(self.points[stick[0]][:2], self.points[stick[1]][:2])
            dis_dif = stick[2] - dis
            mv_ratio = dis_dif / dis / 2
            dx = self.points[stick[1]][0] - self.points[stick[0]][0]
            dy = self.points[stick[1]][1] - self.points[stick[0]][1]
            if stick[0] not in self.grounded:
                self.points[stick[0]][0] -= dx * mv_ratio * 0.85
                self.points[stick[0]][1] -= dy * mv_ratio * 0.85
            if stick[1] not in self.grounded:
                self.points[stick[1]][0] += dx * mv_ratio * 0.85
                self.points[stick[1]][1] += dy * mv_ratio * 0.85

    def render_polygon(self, target_surf, color, offset=[0, 0]):
        y_points = [p[1] * self.scale for p in self.points]
        x_points = [p[0] * self.scale for p in self.points]
        min_x = min(x_points)
        max_x = max(x_points)
        min_y = min(y_points)
        max_y = max(y_points)
        width = int(max_x - min_x + 2)
        height = int(max_y - min_y + 2)
        surf = pygame.Surface((width, height))
        self.render_sticks(surf, (int(min_x), int(min_y)))
        surf.set_colorkey((0, 0, 0))
        m = pygame.mask.from_surface(surf)
        outline = m.outline() # get outline of mask
        surf.fill((0, 0, 0)) # fill with color that will be colorkey
        surf.set_colorkey((0, 0, 0))
        pygame.draw.polygon(surf, color, outline)
        target_surf.blit(surf, (min_x - offset[0], min_y - offset[1]))

    def render_sticks(self, surf, offset=[0, 0]):
        render_points = [[p[0] * self.scale - offset[0], p[1] * self.scale - offset[1]] for p in self.points]
        for stick in self.sticks:
            pygame.draw.line(surf, (255, 255, 255), render_points[stick[0]], render_points[stick[1]], 1)
