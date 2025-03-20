import Constants
import pygame

global sprites
pygame.init()
pygame.display.set_mode((0,0))
sprites=Constants.spritesheets.return_character_spritesheets2(5)

class Rigged_Character():
    
    def __init__(self):
        
        self.idleanims,self.kickanims,self.attackanims,self.hurtanims,self.walkanims,self.runanims,self.pushanims,self.pullanims,self.jumpanims,self.winanims,self.dieanims,self.sitanims=sprites
        self.anims={
            'idle':self.idleanims,
            'kick':self.kickanims,
            'attack':self.attackanims,
            'hurt':self.hurtanims,
            'walk':self.walkanims,
            'run':self.runanims,
            'push':self.pushanims,
            'pull':self.pullanims,
            'jump':self.jumpanims,
            'win':self.winanims,
            'die':self.dieanims,
            'sit':self.sitanims
        }
        self.animnum=0
        self.animmode='idle'
        
    def update_rig(self):
        if self.animmode in ['idle','kick','attack','hurt']:
            self.animnum+=1
            if self.animnum>=2:
                self.animnum=0
        elif self.animmode in ['walk','run','push','pull','win']:
            self.animnum+=1
            if self.animnum>=4:
                self.animnum=0
        elif self.animmode in ['jump']:
            self.animnum+=1
            if self.animnum>=8:
                self.animnum=0
        elif self.animmode in ['die']:
            if self.animnum<3:
                self.animnum+=1
        elif self.animmode in ['sit']:
            if self.animnum<1:
                self.animnum+=1
        
        return self.anims[self.animmode][self.animnum]
    
    def set_anim(self,mode):
        self.animmode=mode
        self.animnum=0
        
    def cycle_anim_list(self):
        modelist=list(self.anims.keys())
        try:
            self.set_anim(modelist[modelist.index(self.animmode)+1])
        except:
            self.set_anim(modelist[0])