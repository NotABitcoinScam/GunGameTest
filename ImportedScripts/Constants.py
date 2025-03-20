import pygame

class OLDspritesheets():
    
    def get_img(spritesheet,x,y,w,h,scale=1,color=(0,0,0)):
        img=pygame.Surface([w-x,h-y]).convert()
        img.blit(spritesheet,(0,0),(x,y,w,h))
        img.set_colorkey(color)
        img=pygame.transform.scale(img,(img.get_width()*scale,img.get_height()*scale))
        return img
        
    def return_character_spritesheets(scale=1):
        
        mainsheet=pygame.image.load('Assets/CharacterAnims.png')
        mainsheet.set_colorkey((100,100,100))
        y=0
        idleanims=[spritesheets.get_img(mainsheet,32*i,0+y,32*i+32,32+y,scale) for i in range(4)]
        y+=32
        runninganims=[spritesheets.get_img(mainsheet,32*i,0+y,32*i+32,32+y,scale) for i in range(4)]
        y+=32
        jumpinganims=[spritesheets.get_img(mainsheet,32*i,0+y,32*i+32,32+y,scale) for i in range(3)]
        y+=32
        rollinganims=[spritesheets.get_img(mainsheet,32*i,0+y,32*i+32,32+y,scale) for i in range(4)]
        y+=32
        hurtanims=[spritesheets.get_img(mainsheet,32*i,0+y,32*i+32,32+y,scale) for i in range(3)]
        y+=32
        deathanims=[spritesheets.get_img(mainsheet,32*i,0+y,32*i+32,32+y,scale) for i in range(4)]
        y+=32
        sleepanims=[spritesheets.get_img(mainsheet,32*i,0+y,32*i+32,32+y,scale) for i in range(3)]
        
        return [idleanims,runninganims,jumpinganims,rollinganims,hurtanims,deathanims,sleepanims]
    
    def return_tile_spritesheets(scale=1):
        
        mainsheet=pygame.image.load('Assets/Tiles/TilesMain.png') 
        tiles=[]
        for q in range(6):
            tileset=[]
            set=spritesheets.get_img(mainsheet,q*40,0,q*40+40,40)
            for y in range(5):
                row=[]
                for x in range(5):
                    row.append(spritesheets.get_img(set,x*8,y*8,
                                                              x*8+8,y*8+8,scale))
                tileset.append(row)
            tiles.append(tileset)
        return tiles
    
    
    def return_tile_spritesheets2(scale=1):
        #Color (57,41,70)
        #Cavernas tile set
        
        # ===== EXTRACTION OF SPRITE SETS =====
        mainsheet=pygame.image.load('Assets/Tiles/Tileset2Copy.png')
        mainsheet.set_colorkey((100,100,100))
        ground1=spritesheets.get_img(mainsheet,24,8,56,32)
        ground2=spritesheets.get_img(mainsheet,24,48,56,72)
        foliage1=spritesheets.get_img(mainsheet,8,0,72,8)
        rocks1=spritesheets.get_img(mainsheet,24,40,72,48)
        hangingfoliage1=spritesheets.get_img(mainsheet,24,32,56,40)
        hangingrocks1=spritesheets.get_img(mainsheet,24,72,56,80)
        
        # ===== GROUND SETS 1 & 2 =====
        groundset1=[]
        for y in range(3):
            row=[]
            for x in range(4):
                row.append(spritesheets.get_img(ground1,x*8,y*8,8+x*8,8+y*8,scale))
            groundset1.append(row)
        
        groundset2=[]
        for y in range(3):
            row=[]
            for x in range(4):
                row.append(spritesheets.get_img(ground2,x*8,y*8,8+x*8,8+y*8,scale))
            groundset2.append(row)
            
        # ===== FOLIAGE & ROCK SETS =====
        foliageset1=[]
        for x in range(8):
            foliageset1.append(spritesheets.get_img(foliage1,x*8,0,8+x*8,8,scale))
            
        rockset1=[]
        for x in range(6):
            rockset1.append(spritesheets.get_img(rocks1,x*8,0,8+x*8,8,scale))
            
        # ===== HANGING FOLIAGE & ROCK SETS =====
        hangingfoliageset1=[]
        for x in range(4):
            hangingfoliageset1.append(spritesheets.get_img(hangingfoliage1,x*8,0,8+x*8,8,scale))
            
        hangingrockset1=[]
        for x in range(4):
            hangingrockset1.append(spritesheets.get_img(hangingrocks1,x*8,0,8+x*8,8,scale))
            
        # ===== RETURN SPRITE LIST =====
        return [groundset1,groundset2,foliageset1,rockset1,hangingfoliageset1,hangingrockset1]
    
    def return_character_spritesheets2(scale=1):
        
        mainsheet=pygame.image.load('Assets/AnimationSheetCopy.png')
        #mainsheet.set_colorkey((100,100,100))
        # ===== ROW 1 =====
        idle=spritesheets.get_img(mainsheet,0,0,48,24,color=(100,100,100))
        kick=spritesheets.get_img(mainsheet,48,0,96,24,color=(100,100,100))
        attack=spritesheets.get_img(mainsheet,96,0,144,24,color=(100,100,100))
        hurt=spritesheets.get_img(mainsheet,144,0,192,24,color=(100,100,100))
        # ===== ROW 2 =====
        walk=spritesheets.get_img(mainsheet,0,24,96,48,color=(100,100,100))
        run=spritesheets.get_img(mainsheet,96,24,192,48,color=(100,100,100))
        # ===== ROW 3 =====
        push=spritesheets.get_img(mainsheet,0,48,96,72,color=(100,100,100))
        pull=spritesheets.get_img(mainsheet,96,48,192,72,color=(100,100,100))
        # ===== ROW 4 =====
        jump=spritesheets.get_img(mainsheet,0,72,192,96,color=(100,100,100))
        # ===== ROW 5 =====
        win=spritesheets.get_img(mainsheet,0,96,96,120,color=(100,100,100))
        die=spritesheets.get_img(mainsheet,96,96,192,120,color=(100,100,100))
        # ===== ROW 6 =====
        sit=spritesheets.get_img(mainsheet,0,120,48,144,color=(100,100,100))
        
        
        
        return [idle,kick,attack,hurt,walk,run,push,pull,jump,win,die,sit]
    
    def return_fireparticles1(scale=1):
        mainsheet=pygame.image.load('Assets/FireParticles1.png')
        particles=[]
        for i in range(4):
            particles.append(spritesheets.get_img(mainsheet,i*8,0,i*8+8,8,scale,(100,100,100)))
        return particles
    
    
    
class spritesheets():
    
    def get_img(spritesheet,x,y,w,h,scale=1,color=(0,0,0)):
        img=pygame.Surface([w-x,h-y]).convert()
        img.blit(spritesheet,(0,0),(x,y,w,h))
        img.set_colorkey(color)
        img=pygame.transform.scale(img,(img.get_width()*scale,img.get_height()*scale))
        return img
    
    def get_main_biome_sheet(file,color=(255,255,255),scale=1):
        
        mainsheet=pygame.image.load(file)
        
        outsidewateredgessheet1=spritesheets.get_img(mainsheet,16,80,64,128)
        outsidwateredges1=[
            [spritesheets.get_img(outsidewateredgessheet1,0,0,16,16,scale=scale,color=color),
            spritesheets.get_img(outsidewateredgessheet1,16,0,32,16,scale=scale,color=color),
            spritesheets.get_img(outsidewateredgessheet1,32,0,48,16,scale=scale,color=color)],
            
            [spritesheets.get_img(outsidewateredgessheet1,0,16,16,32,scale=scale,color=color),
            spritesheets.get_img(outsidewateredgessheet1,16,16,32,32,scale=scale,color=color),
            spritesheets.get_img(outsidewateredgessheet1,32,16,48,32,scale=scale,color=color)],
            
            [spritesheets.get_img(outsidewateredgessheet1,0,32,16,48,scale=scale,color=color),
            spritesheets.get_img(outsidewateredgessheet1,16,32,32,48,scale=scale,color=color),
            spritesheets.get_img(outsidewateredgessheet1,32,32,48,48,scale=scale,color=color)]
        ]
        
        outsidecliffedgessheet1=spritesheets.get_img(mainsheet,16,16,96,80)
        outsidecliffedges1=[
            [spritesheets.get_img(outsidecliffedgessheet1,0,0,16,16,scale=scale,color=color),
            spritesheets.get_img(outsidecliffedgessheet1,16,0,32,16,scale=scale,color=color),
            spritesheets.get_img(outsidecliffedgessheet1,32,0,48,16,scale=scale,color=color),
            spritesheets.get_img(outsidecliffedgessheet1,48,0,64,16,scale=scale,color=color),
            spritesheets.get_img(outsidecliffedgessheet1,64,0,80,16,scale=scale,color=color)],
            
            [spritesheets.get_img(outsidecliffedgessheet1,0,16,16,32,scale=scale,color=color),
            spritesheets.get_img(outsidecliffedgessheet1,16,16,32,32,scale=scale,color=color),
            spritesheets.get_img(outsidecliffedgessheet1,32,16,48,32,scale=scale,color=color),
            spritesheets.get_img(outsidecliffedgessheet1,48,16,64,32,scale=scale,color=color),
            spritesheets.get_img(outsidecliffedgessheet1,64,16,80,32,scale=scale,color=color)],
            
            [spritesheets.get_img(outsidecliffedgessheet1,0,32,16,48,scale=scale,color=color),
            spritesheets.get_img(outsidecliffedgessheet1,16,32,32,48,scale=scale,color=color),
            spritesheets.get_img(outsidecliffedgessheet1,32,32,48,48,scale=scale,color=color),
            spritesheets.get_img(outsidecliffedgessheet1,48,32,64,48,scale=scale,color=color),
            spritesheets.get_img(outsidecliffedgessheet1,64,32,80,48,scale=scale,color=color)],
            
            [spritesheets.get_img(outsidecliffedgessheet1,0,48,16,64,scale=scale,color=color),
            spritesheets.get_img(outsidecliffedgessheet1,16,48,32,64,scale=scale,color=color),
            spritesheets.get_img(outsidecliffedgessheet1,32,48,48,64,scale=scale,color=color),
            spritesheets.get_img(outsidecliffedgessheet1,48,48,64,64,scale=scale,color=color),
            spritesheets.get_img(outsidecliffedgessheet1,64,48,80,64,scale=scale,color=color)]
        ]
        
        innermainsheet1=spritesheets.get_img(mainsheet,160,16,192,80)
        innermain1=[
            [spritesheets.get_img(innermainsheet1,0,0,16,16,scale=scale,color=color),
            spritesheets.get_img(innermainsheet1,16,0,32,16,scale=scale,color=color)],
            
            [spritesheets.get_img(innermainsheet1,0,16,16,32,scale=scale,color=color),
            spritesheets.get_img(innermainsheet1,16,16,32,32,scale=scale,color=color)],
            
            [spritesheets.get_img(innermainsheet1,0,32,16,48,scale=scale,color=color),
            spritesheets.get_img(innermainsheet1,16,32,32,48,scale=scale,color=color)],
            
            [spritesheets.get_img(innermainsheet1,0,48,16,64,scale=scale,color=color),
            spritesheets.get_img(innermainsheet1,16,48,32,64,scale=scale,color=color)]
        ]
        
        insidewateredgessheet1=spritesheets.get_img(mainsheet,64,80,96,112)
        insidewateredges1=[
            [spritesheets.get_img(insidewateredgessheet1,0,0,16,16,scale=scale,color=color),
            spritesheets.get_img(insidewateredgessheet1,16,0,32,16,scale=scale,color=color)],
            
            [spritesheets.get_img(insidewateredgessheet1,0,16,16,32,scale=scale,color=color),
            spritesheets.get_img(insidewateredgessheet1,16,16,32,32,scale=scale,color=color)],
        ]
        
        return [outsidwateredges1,outsidecliffedges1,innermain1,insidewateredges1]
        
    
    def return_character_spritesheets2(scale=1):
        
        mainsheet=pygame.image.load('Assets/AnimationSheetCopy.png')
        # ===== ROW 1 =====
        idle=spritesheets.get_img(mainsheet,0,0,48,24,color=None)
        kick=spritesheets.get_img(mainsheet,48,0,96,24,color=None)
        attack=spritesheets.get_img(mainsheet,96,0,144,24,color=None)
        hurt=spritesheets.get_img(mainsheet,144,0,192,24,color=None)
        # ===== ROW 2 =====
        walk=spritesheets.get_img(mainsheet,0,24,96,48,color=None)
        run=spritesheets.get_img(mainsheet,96,24,192,48,color=None)
        # ===== ROW 3 =====
        push=spritesheets.get_img(mainsheet,0,48,96,72,color=None)
        pull=spritesheets.get_img(mainsheet,96,48,192,72,color=None)
        # ===== ROW 4 =====
        jump=spritesheets.get_img(mainsheet,0,72,192,96,color=None)
        # ===== ROW 5 =====
        win=spritesheets.get_img(mainsheet,0,96,96,120,color=None)
        die=spritesheets.get_img(mainsheet,96,96,192,120,color=None)
        # ===== ROW 6 =====
        sit=spritesheets.get_img(mainsheet,0,120,48,144,color=None)
        
        
        idleanims=[]
        for i in range(2):
            idleanims.append(spritesheets.get_img(idle,i*24,0,i*24+24,24,scale=scale,color=(100,100,100)))
        kickanims=[]
        for i in range(2):
            kickanims.append(spritesheets.get_img(kick,i*24,0,i*24+24,24,scale=scale,color=(100,100,100)))
        attackanims=[]
        for i in range(2):
            attackanims.append(spritesheets.get_img(attack,i*24,0,i*24+24,24,scale=scale,color=(100,100,100)))
        hurtanims=[]
        for i in range(2):
            hurtanims.append(spritesheets.get_img(hurt,i*24,0,i*24+24,24,scale=scale,color=(100,100,100)))
        walkanims=[]
        for i in range(4):
            walkanims.append(spritesheets.get_img(walk,i*24,0,i*24+24,24,scale=scale,color=(100,100,100)))
        runanims=[]
        for i in range(4):
            runanims.append(spritesheets.get_img(run,i*24,0,i*24+24,24,scale=scale,color=(100,100,100)))
        pushanims=[]
        for i in range(4):
            pushanims.append(spritesheets.get_img(push,i*24,0,i*24+24,24,scale=scale,color=(100,100,100)))
        pullanims=[]
        for i in range(4):
            pullanims.append(spritesheets.get_img(pull,i*24,0,i*24+24,24,scale=scale,color=(100,100,100)))
        jumpanims=[]
        for i in range(8):
            jumpanims.append(spritesheets.get_img(jump,i*24,0,i*24+24,24,scale=scale,color=(100,100,100)))
        winanims=[]
        for i in range(4):
            winanims.append(spritesheets.get_img(win,i*24,0,i*24+24,24,scale=scale,color=(100,100,100)))
        dieanims=[]
        for i in range(4):
            dieanims.append(spritesheets.get_img(die,i*24,0,i*24+24,24,scale=scale,color=(100,100,100)))
        sitanims=[]
        for i in range(2):
            sitanims.append(spritesheets.get_img(sit,i*24,0,i*24+24,24,scale=scale,color=(100,100,100)))
            
        return [idleanims,kickanims,attackanims,hurtanims,walkanims,runanims,pushanims,pullanims,jumpanims,winanims,dieanims,sitanims]
    
    def return_fireparticles1(scale=1):
        mainsheet=pygame.image.load('Assets/FireParticles1.png')
        particles=[]
        for i in range(4):
            particles.append(spritesheets.get_img(mainsheet,i*8,0,i*8+8,8,scale,(100,100,100)))
        return particles