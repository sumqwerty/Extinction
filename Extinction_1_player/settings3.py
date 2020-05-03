import pygame as pg
vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
BLUE = (0, 0, 255)
LIGHT_BLUE = (100,100,255)
GREEN = (0, 255, 0)
DARK_GREEN = (34, 177, 76)
RED = (255, 0, 0)
DARK_RED = (200, 0 ,0)
YELLOW = (255, 255, 0)
DARK_YELLOW = (200,200,0)
BROWN = (106, 55, 5)
CYAN = (0, 255, 255)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 704
FPS = 60
ICON_IMG = 'zicon.png'
TITLE = "Extinction"
BGCOLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
#PLAYER_HEALTH decided when selected
PLAYER_SPEED = 280 #default
PLAYER_ROT_SPEED = 200 #defaut
PLAYER_IMG = ['manBlue_gun.png', 'soldier1_machine.png', 'hitman1_silencer.png', 'robot1_machine.png', 'manBrown_gun.png', 'survivor1_silencer.png']

##PLAYER_IMG_BLUE = ['manBlue_gun.png', 'manBlue_machine.png', 'manBlue_silencer.png']
##PLAYER_IMG_SLODIER = ['manBlue_gun.png', 'soldier1_machine.png', 'hitman1_silencer.png', 'robot1_machine.png', 'manBrown_gun.png', 'survivor1_silencer.png']
##PLAYER_IMG_HITMAN = ['manBlue_gun.png', 'soldier1_machine.png', 'hitman1_silencer.png', 'robot1_machine.png', 'manBrown_gun.png', 'survivor1_silencer.png']
##PLAYER_IMG_ROBOT = ['manBlue_gun.png', 'soldier1_machine.png', 'hitman1_silencer.png', 'robot1_machine.png', 'manBrown_gun.png', 'survivor1_silencer.png']
##PLAYER_IMG_BROWN = ['manBlue_gun.png', 'soldier1_machine.png', 'hitman1_silencer.png', 'robot1_machine.png', 'manBrown_gun.png', 'survivor1_silencer.png']
##PLAYER_IMG_SURVIVOR = ['manBlue_gun.png', 'soldier1_machine.png', 'hitman1_silencer.png', 'robot1_machine.png', 'manBrown_gun.png', 'survivor1_silencer.png']

HEALTH_IMG = ['blue.png','sol.png', 'hit.png', 'rob.png', 'Brown.png', 'sur.png']
HEALTH_IMG_REAL = ['blue_rl.jpg','sol_rl.jpg', 'hit_man_rl.jpg', 'rob_rl.jpg', 'brown_rl.jpg', 'sur_rl.jpg']
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# Weapon settings

BULLET_IMG = 'bullet.png'
ROCKET_IMG = 'NES.png'
IMGS = ['pistol.png','shotgun.png','rocketlauncher.png']
BIMGS = ['ammo_pistol.png','ammo_shotgun.png','ammo_rocket.png']

WEAPONS = {}

WEAPONS['pistol'] = {'bullet_speed': 500,
                     'bullet_lifetime': 1000,
                     'rate': 250,
                     'kickback': 200,
                     'spread': 5,
                     'damage': 10,
                     'bullet_size': 'lg',
                     'bullet_count': 1,
                     'ammo': 6,
                     'full_ammo': 6}    #default

WEAPONS['shotgun'] = {'bullet_speed': 400,
                      'bullet_lifetime': 500,
                      'rate': 600,
                      'kickback': 300,
                      'spread': 20,
                      'damage': 10,
                      'bullet_size': 'sm',
                      'bullet_count': 12,
                      'ammo': 12,
                      'full_ammo': 12} #default

WEAPONS['pistol_z'] = {'bullet_speed': 600,
                     'bullet_lifetime': 1000,
                     'rate': 600,
                     'kickback': 0,
                     'spread': 5,
                     'damage': 10,
                     'bullet_size': 'lg',
                     'bullet_count': 1,
                     'ammo': 6,
                     'full_ammo': 6}    #default

WEAPONS['rocket'] = {'bullet_speed': 1000,
                      'bullet_lifetime': 700,
                      'rate': 1000,
                      'kickback': 700,
                      'spread': 10,
                      'damage': 50,
                      'bullet_size': 'rk',
                      'bullet_count': 1,
                      'ammo': 4,
                      'full_ammo': 4} #default



# Mob settings1
MOB_IMG = 'zoimbie1_hold.png'
MOB_SPEEDS = [150, 100, 75, 125]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 10 #defaut
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 400

BOSS_IMG = 'boss.png'
BOSS_SPEEDS = 400
BOSS_HIT_RECT = pg.Rect(5, 0, 45, 45)
BOSS_HEALTH = 600
BOSS_DAMAGE = 15 #defaut
BOSS_KNOCKBACK = 20
BOSS_DETECT_RADIUS = 600


BIG_BOSS_IMG = 'big_boss.png'
BIG_BOSS_SPEEDS = 500
BIG_BOSS_HIT_RECT = pg.Rect(5, 0, 45, 45)
BIG_BOSS_HEALTH = 600
BIG_BOSS_DAMAGE = 15 #defaut
BIG_BOSS_KNOCKBACK = 40
BIG_BOSS_DETECT_RADIUS = 1000





# Effects
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png',
                  'whitePuff18.png']
SPLAT = 'splat green.png'
FLASH_DURATION = 50
DAMAGE_ALPHA = [i for i in range(0, 255, 55)]
NIGHT_COLOR = (20, 20, 20)
LIGHT_RADIUS = (500, 500)
LIGHT_MASK = "light_350_soft.png"

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

# Items
ITEM_IMAGES = {'health': 'health_pack.png',
               'shotgun': 'obj_shotgun.png',
               'rocket': 'rckt.png',
               'am_box': 'Ammo_Box.png'}
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 10
BOB_SPEED = 0.3

# Sounds
BG_MUSIC = 'espionage.ogg'
PLAYER_HIT_SOUNDS = ['pain/8.wav', 'pain/9.wav', 'pain/10.wav', 'pain/11.wav']
ZOMBIE_MOAN_SOUNDS = ['brains2.wav', 'brains3.wav', 'zombie-roar-1.wav', 'zombie-roar-2.wav',
                      'zombie-roar-3.wav', 'zombie-roar-5.wav', 'zombie-roar-6.wav', 'zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
WEAPON_SOUNDS = {'pistol': ['pistol.wav'],
                 'shotgun': ['shotgun.wav'],
                 'rocket': ['BAZOOKA.wav'],
                 'pistol_z': ['pistol.wav']}
EFFECTS_SOUNDS = {'level_start': 'level_start.wav',
                  'health_up': 'health_pack.wav',
                  'gun_pickup': 'gun_pickup.wav'}
