# Project Name: Vehicles

## Idea:
Vehicles is a system that supposed to be a single reference that has all information about Cars, Brands, Classes, Categories ...etc, that gives an opportunity to whom it may concern to add, manage thier brand like "Ford Motor Company", also gives an opportunity to whoever wants to search,compare between cars and brands like entities or individuals.

This system can also grow to contain more information about cars, or even more information about other vehicles like (Plains, SHips, Trains, Motocycle).


## Inspiration:
Django RESTful Framework training course provided by "Tuwaiq" made this course so intriguing that inspired
me to start a project that can be big and challenging so I would have experienced a lot of programming aspects if I continue the journey after this course ended>.

## List of Services / Features:

- Adds and manages information about variety Brands of cars.
- Adds and manages cars informations.
- Catigorizes cars in deffirent classes and catigories.
- Manage the users of this system.


## Type of users: 
    - Admin users: have full CRUD auth/perm to manage all models, users.
    - Stuff users:
        - Brands Group : have full CRUD auth/perm to manage Brand/BrandsClasses model.
        - GeneralClasses Group : have full CRUD auth/perm to manage GeneralClasses model.
        - Categories Group : have full CRUD auth/perm to manage Categories model.
        - Cars Group : have full CRUD auth/perm to manage Car model.
    - Ordinary Users: have only search/show cars information.
    - Anonymous Users: show cars information with no other options like search.

### Cars app

- Create, Read, Update, Delete Brands records. Brand (Ford, Mercedes-Benz, Toyota....etc)
- Save a record of every add/update that took place in brands model.
- Create, Read, Update, Delete GeneralClasses records. Classes like ()
- Create, Read, Update, Delete BrandsClasses records. BrandsClasses like (Luxury cars ,Commercial cars, sport cars ... etc)
- Create, Read, Update, Delete Categories records. Categories like (sedan car, Family car, 4x4 car, Truks, industiral cars ... etc.)
- Create, Read, Update, Delete Car records. Cars like ()

### Users app

- An independent app to Create, Read, Update, and Delete users.