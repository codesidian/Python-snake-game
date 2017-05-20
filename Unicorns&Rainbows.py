"""
TODO:
-SCORING - DONE
-SOUND (Don't have repeating sounds)  - DONE
"""
import pygame,time,random,sys

pygame.init()

#####################Colours#####################
white = (255,255,255)
grey = (170,170,170)
black = (0,0,0)
cyan=(0,255,255)
red = (255,0,0)
green = (0,255,0)
darkGreen = (0,155,0)

blue = (0,0,255)

#####################Display Variables#####################
display_width=800
display_height=600
gameDisplay = pygame.display.set_mode((display_width,display_height),0,32)

#####################Misc variables#####################
pygame.display.set_caption('Unicorns & Rainbows')
FPS=24
font = pygame.font.SysFont(None, 25)
clock = pygame.time.Clock()
mainmenucalled=0



#####################Images#####################
#Backgrounds
bg = pygame.image.load("bg1.jpg")

gameoverbg = pygame.image.load("gameover1.jpg")
mainmenubg = pygame.image.load("mainmenubg.jpg")
#unicorn
unicornPicR= pygame.image.load("unicornR.png")
unicornPicL= pygame.image.load("unicornL.png")
unicornPicU= pygame.image.load("unicornU.png")
unicornPicD= pygame.image.load("unicornD.png")
#rainbow(Or cookie)
rainbowPic= pygame.image.load("rainbow2.png")
#following rainbow
rainbowFollowingPicR= pygame.transform.scale((pygame.image.load("rainbowR.png")), (20,20))
rainbowFollowingPicL= pygame.transform.scale((pygame.image.load("rainbowL.png")), (20,20))
rainbowFollowingPicU= pygame.transform.scale((pygame.image.load("rainbowU.png")), (20,20))
rainbowFollowingPicD= pygame.transform.scale((pygame.image.load("rainbowD.png")), (20,20))
#misc images
icon = pygame.image.load("rainbow2.png")
pygame.display.set_icon(icon)
#####################Sound#####################
pygame.mixer.init()
pygame.mixer.set_num_channels(8)

musicChan = pygame.mixer.Channel(5)
endChan = pygame.mixer.Channel(6)

chomp=pygame.mixer.Sound("Chomp.wav")
end=pygame.mixer.Sound("end.wav")
hit=pygame.mixer.Sound("hit.wav")
music=pygame.mixer.Sound("music.wav")

def textToScreen(text,colour,xtext=0,ytext=0):

    screenText = font.render(text,True,colour)
    gameDisplay.blit(screenText, [xtext,ytext])

def unicorn(playerPos_x,playerPos_y,block_size,unicornList,unicornPic,rainbowFollowingPic):
    for XnY in unicornList[:-1]:
         
         gameDisplay.blit(rainbowFollowingPic,(XnY[0]+20,XnY[1]+20))   
         #pygame.draw.rect(gameDisplay,red,[XnY[0],XnY[1],block_size,block_size])
        
    gameDisplay.blit(unicornPic,(unicornList[-1][0],unicornList[-1][1])) 
     
       


def gameLoop(mainmenucalled,FPS ):
    endChan.fadeout(6)

    #####################PlayerVariables#####################
    playerPos_x=display_width/2
    playerPos_x_change=0
    playerPos_y=display_height/2
    playerPos_y_change=0

    block_size=50
    unicorn_speed=15

    unicornList =[]
    unicornLength = 1
    unicornPic=unicornPicR

    left=0
    right=0
    up=0
    down=0

    score=0

    rainbowFollowingPic=rainbowFollowingPicR
    
    #####################Misc Variables#####################
    gameExit=False
    gameOver=False
    mainmenu=True
    FPS=24
    
    
    

    #rainbowspawning
    randRainX = random.randrange(0, 750)
    randRainY = random.randrange(0, 550)

    
    #Main music
    if musicChan.get_busy()==False:
        musicChan.play(music)

    


    #Main menu
    if mainmenucalled==0:
        
        mainmenucalled=1
        while mainmenu==True:
            gameDisplay.blit(mainmenubg,(0,0))  
           
            pygame.display.update()
         

            for event in pygame.event.get():
                #print(event)
                
                if event.type == pygame.QUIT:
                   gameExit=True
                   gameOver=False
                   mainmenu=False
                   
                   
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit=True
                        gameOver=False
                        mainmenu=False
                        
                    if event.key == pygame.K_SPACE:
                        gameLoop(mainmenucalled,FPS )
        
    #game over screen if game Exit is true, just exit the game
    while not gameExit:
        

        while gameOver==True:
            
            
            gameDisplay.blit(gameoverbg,(0,0))  
           
            pygame.display.update()
         

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   gameExit=True
                   gameOver=False
                   
                   
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit=True
                        gameOver=False
                    if event.key == pygame.K_SPACE:
                        gameLoop(mainmenucalled,FPS )
                        

        #Checking for events
        for event in pygame.event.get():
            #QUITING
           if event.type == pygame.QUIT:
               
               gameExit=True
               
               

            #ARROW KEY  MOVEMENT
           if event.type == pygame.KEYDOWN:
               
                   #left key
                if event.key == pygame.K_LEFT and right ==0:
                    playerPos_x_change=-unicorn_speed
                    playerPos_y_change=0
                    unicornPic=unicornPicL
                    left=1
                    right=0
                    up=0
                    down=0
                    rainbowFollowingPic=rainbowFollowingPicL
                    
                    #right key
                elif event.key == pygame.K_RIGHT and left==0:
                    playerPos_x_change=unicorn_speed
                    playerPos_y_change=0
                    unicornPic=unicornPicR
                    left=0
                    right=1
                    up=0
                    down=0
                    rainbowFollowingPic=rainbowFollowingPicR
                    
                    #up key
                elif event.key == pygame.K_UP and down==0:
                    playerPos_y_change=-unicorn_speed
                    playerPos_x_change=0
                    unicornPic=unicornPicU
                    right=0
                    left=0
                    up=1
                    down=0
                    rainbowFollowingPic=rainbowFollowingPicU
                    
                    #down key
                elif event.key == pygame.K_DOWN and up==0:
                    playerPos_y_change=unicorn_speed
                    playerPos_x_change=0
                    unicornPic=unicornPicD
                    right=0
                    left=0
                    up=0
                    down=1
                    rainbowFollowingPic=rainbowFollowingPicD
                elif event.key == pygame.K_m:
                    pygame.mixer.music.pause()
             

        #moving player
        playerPos_x+=playerPos_x_change
        playerPos_y+=playerPos_y_change
                    

        #Checking if the player is out of the window boundaries. 
        if playerPos_x>=display_width or playerPos_x<=0 or playerPos_y>=display_height or playerPos_y<=0:
            
            gameOver=True
            #stop main menu music
            musicChan.fadeout(5)
            
            endChan.play(end)
            
            
        #Drawing the bg
        gameDisplay.blit(bg, (0, 0))
        #drawing score
        textToScreen("Score: " + str(score),cyan,370,10)

        

        #Setting the thickness of the boundary box for the cookie/rainbow
        rainbowThickness=70

         
        
    
        #Adding the XY coords to the unicorn's rainbow list
        unicornHead =[]
        unicornHead.append(playerPos_x)
        unicornHead.append(playerPos_y)
        unicornList.append(unicornHead)

        #deleting the end of the rainbow
        if len(unicornList) > unicornLength:
            del unicornList[0]

            #checking if the unicorn has hit it's tail.
        for eachSegment in unicornList[:-1]:
            if eachSegment == unicornHead:
                
                hit.play()
                
                #Checking if the end noise is playing
                
                endChan.play(end)
           
                musicChan.fadeout(5)
                gameOver=True
        #drawing the cookie
        gameDisplay.blit(rainbowPic,(randRainX,randRainY))
        #Drawing the unicorn and the tail
        unicorn(playerPos_x,playerPos_y,block_size,unicornList,unicornPic,rainbowFollowingPic)
        
        pygame.display.update()


        #Checking to see if the unicorn has entered the dimensions of the cookie 
        if playerPos_x >= randRainX and playerPos_x < randRainX+rainbowThickness or playerPos_x+block_size > randRainX and playerPos_x + block_size < randRainX + rainbowThickness:
            if playerPos_y >= randRainY and playerPos_y < randRainY+rainbowThickness or playerPos_y+block_size > randRainY and playerPos_y + block_size < randRainY + rainbowThickness:
                    randRainX = random.randrange(50, 750)
                    randRainY = random.randrange(50, 550)
                    unicornLength+=2
                    FPS+=0.5
                    score+=10
                    
                    chomp.play()
                    
                    


        clock.tick(FPS)



    pygame.quit()
    quit()

gameLoop(mainmenucalled,FPS )
