### Fetch all charging station of France

### 1st idea : grid fetch
>   Data provided - then remoduled - by file from [Graydon](https://gist.github.com/graydon/11198540)
>   gives the limits including DOM-TOM, but we want metropolitan coordinates 


>   Data found on [wikipédia](https://fr.wikipedia.org/wiki/Liste_de_points_extr%C3%AAmes_de_la_France)
>  ! Given in time

> point le + au nord : 51 05 21  
> point le + au sud : 42 19 58  
> point le + a l'est : 8 13 50  
> point le + a l'ouest : (-) 4 47 44

| Degré | Minute | Seconde |  latitude   |  longitude  |
|------:|-------:|--------:|:-----------:|:-----------:|
|    51 |     05 |      21 | 51.08916667 |      X      |
|    42 |     19 |      58 | 42.33277778 |      X      |
|     8 |     13 |      50 |      X      | 8.23055556  |
|    -4 |     47 |      44 |      X      | -4.79555556 |

bounding box of France : (51.08916667 , -4.79555556) <=> (42.33277778 ,8.23055556 )

latitude range : 8,75 638 889
longitude range  : 13,02 611 112

parameter tuning : 1st scale using 100x100 grid ( = 10 000 cases)







{
    "width" : 100,
    "height" : 100,
    "coordinates": {
        "origin": {
            "lat":4233277778,
            "lon":823055556
        },
        "dest" : {
            "lat":5108916667,
            "lon":-479555556
        },
        "current" : {
            "lat":4233277778,
            "lon":823055556
        }
    }
}

define width and height
radius of search 1km (diameter 2km)
gap between 2circles in diagonal : 820m
== get diagonaly closer (410m each)
410diagonal = 289m following y and 289m following x

leads to 1call with radius 1km every (2 * 1km  - 289m) 1700m
northest point <-> southest point : 1000km
eastest point <-> westest point : 910km

1000 / 1,7 = 590
910 / 1,7 = 535

590*535 = 315 823api calls

1 call ~~ every 4s (315823*4  => 1 263 294s = 350h = 14d)
1 call ~~ every 3s (315823*3  => 947 469s = 263h = 11d)
