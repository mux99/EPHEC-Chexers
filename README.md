# EPHEC-T201-Dammes

## Synopsis
This is a school project, meant to create a game of *checkers* with extra rules. Apparently this group don't seem to bother with easy, so we went with an hexagonal grid. On top of that, we added teleportation (yes otherwise it's not confusing enough). Finally we went with a graphical interface despite the requirements beeing only for a console base game. We tried it, it's unplayable in console.

### 'Client' Needs
The client (the teacher realy) wanted a game of checkers to play locally with a friend. It also needed to give a score to each players and save them to a file. Yes it is the sole reason we added a scoreboard. Appart from that we were free.
A prototype was to be realise in two week, since we dirrectly went for a graphical interface. We didnt have the console interface that aparently was needed. So the one present on the **console branch** has been done in 4 hours and hasn't been updated since. Please don't use it.

## Game rules
- the whites begin
- the pieces can move in diagonal  
Image![alt text](https://cdn.discordapp.com/attachments/1031895995648323606/1042461142343225404/mvt.png)  
- the pieces can take both pieces surrounding a move and move backwards to take  
Image![alt text](https://cdn.discordapp.com/attachments/1031895995648323606/1042461142649417738/prise.png)  
- when a piece reaches the opposite end of the board it is promoted to queen
- a queen can move any number of free tiles, in any directions
- when on a green tile, a piece can warp to the other side of the board
- when multiples takes in a row can be made, they are mandatory
- (TBD) when a player can take a piece, he must do so
- (TBD) the moves that will result in the most takes (in a row) is mandatory

at the end of the game, the scoreboard (local) will aprear:
- enter the name of the winner
- press [enter]
- enter the name of the looser
- press [enter]
scores are then saved.  
if you enter the same name with a better score, you will overwrite older one (logical, I know)

## Scores
pray the eldritch gods to be favored by the uptruce algorithm

## How to install?
### Requirements
- **python 3** installed
- the **pyglet** library (tested with version 1.5 to 2.1)

### Run
download the archive and run **main.py**   
a window will open, you simply play by clicking

## How does it work?
### Coordonates
Since we didn't know what kind of rules we were going to need to make it work, we went for the more versatile option for hexagonal grids: cube coordonates. Those have one rule, **x**+**y**+**z**=**0**
To briefly explain, the grid is composed of *3* axis *60°* from each other. The x axis is easy, it is vertical going up.
The other two are a bit more complicated but with some trigonometry it's dooable. Again see link bellow for more infos.

### Warp
For implementing warps from one side of the board to the other (only horizontaly), we simply teleport any future position that is outside the board to the other side.

### Scoreboard
The scoreboard is fully local. It always writes and read to the same file. If a name that already exist is entered, the best score is kept. The file is sorted each time it is written to. The file is read once at lauch, any change after won't register. They will be erased when new scores are saved.

## Authors
Dourov Maxime   
CRUQUENAIRE Achille   
GENDEBIEN Jonas

## Acknowledgments

hexagonal grid calculations: [here](https://www.redblobgames.com/grids/hexagons/)
