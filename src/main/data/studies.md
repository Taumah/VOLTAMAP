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
