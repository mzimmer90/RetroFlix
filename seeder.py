from application import db, Actor, Genre, Film, TVSeries, TVSeriesSeason, TVSeriesEpisode, User, CardDetail, Subscription, Login, FilmViews, Retention
from application import app
from werkzeug.security import generate_password_hash
from random import randint, choice
from datetime import datetime, timedelta
from faker import Faker

# Create actors

sam_neill = Actor(name='Sam Neill')
laura_dern = Actor(name='Laura Dern')
jeff_goldblum = Actor(name='Jeff Goldblum')

zach_galligan = Actor(name='Zach Galligan')
phoebe_cates = Actor(name='Phoebe Cates')
hoyt_axton = Actor(name='Hoyt Axton')

bill_murray = Actor(name='Bill Murray')
dan_aykroyd = Actor(name='Dan Aykroyd')
sigourney_weaver = Actor(name='Sigourney Weaver')

henry_thomas = Actor(name='Henry Thomas')
drew_barrymore = Actor(name='Drew Barrymore')
dee_wallace = Actor(name='Dee Wallace')

harrison_ford = Actor(name='Harrison Ford')
rutger_hauer = Actor(name='Rutger Hauer')
sean_young = Actor(name='Sean Young')

arnold_schwarzenegger = Actor(name='Arnold Schwarzenegger')
michael_biehn = Actor(name='Michael Biehn')
linda_hamilton = Actor(name='Linda Hamilton')

jennifer_aniston = Actor(name='Jennifer Aniston')
lisa_kudrow = Actor(name='Lisa Kudrow')
matt_le_blanc = Actor(name='Matt Le Blanc')

kirstie_alley = Actor(name='Kirstie Alley')
ted_danson = Actor(name='Ted Danson')
rhea_perlman = Actor(name='Rhea Perlman')

kelsey_grammer = Actor(name='Kelsey Grammer')
jane_leeves = Actor(name='Jane Leeves')
john_mahoney = Actor(name='John Mahoney')

ed_oneill = Actor(name="Ed O'Neill")
katy_sagal = Actor(name='Katy Sagal')
christina_applegate = Actor(name='Christina Applegate')

bea_arthur = Actor(name='Bea Arthur')
betty_white = Actor(name='Betty White')
rue_mclanahan = Actor(name='Rue McClanahan')

cybill_shepherd = Actor(name='Cybill Shepherd')
bruce_willis = Actor(name='Bruce Willis')
allyce_beasley = Actor(name='Allyce Beasley')

actors = [
    sam_neill,   
    laura_dern,   
    jeff_goldblum,   
    zach_galligan,   
    phoebe_cates,   
    hoyt_axton,   
    bill_murray,   
    dan_aykroyd,   
    sigourney_weaver,   
    henry_thomas,   
    drew_barrymore,   
    dee_wallace,   
    harrison_ford,   
    rutger_hauer,   
    sean_young,   
    arnold_schwarzenegger,   
    michael_biehn,   
    linda_hamilton,
    jennifer_aniston,
    lisa_kudrow,
    matt_le_blanc,
    kirstie_alley,
    ted_danson,
    rhea_perlman,
    kelsey_grammer,
    jane_leeves,
    john_mahoney,
    ed_oneill,
    katy_sagal,
    christina_applegate,
    bea_arthur,
    betty_white,
    rue_mclanahan,
    cybill_shepherd,
    bruce_willis,
    allyce_beasley
]

# Create genres

action = Genre(genre='Action')
adventure = Genre(genre='Adventure')
comedy = Genre(genre='Comedy')
family = Genre(genre='Family')
fantasy = Genre(genre='Fantasy')
horror = Genre(genre='Horror')
science_fiction = Genre(genre='Science Fiction')
thriller = Genre(genre='Thriller')
sitcom = Genre(genre='Sitcom')
romance = Genre(genre='Romance')
drama = Genre(genre='Drama')
mystery = Genre(genre='Mystery')

genres = [
    action,    
    adventure,    
    comedy,    
    family,    
    fantasy,    
    horror,    
    science_fiction,    
    thriller,
    sitcom,
    romance,
    drama,
    mystery
]

# Create films

jurassic_park = Film(title='Jurassic Park', release_year=1993, duration='02:07:00', age_rating='PG-13', rating=8.2)
gremlins = Film(title='Gremlins', release_year=1984, duration='01:46:00', age_rating='PG', rating=7.3)
ghostbusters = Film(title='Ghostbusters', release_year=1984, duration='01:45:00', age_rating='PG', rating=7.8)
et = Film(title='E T the Extra Terrestrial', release_year=1982, duration='01:55:00', age_rating='PG', rating=7.9)
blade_runner = Film(title='Blade Runner', release_year=1982, duration='01:57:00', age_rating='R', rating=8.1)
terminator = Film(title='The Terminator', release_year=1984, duration='01:47:00', age_rating='R', rating=8.1)

films = [
    jurassic_park,    
    gremlins,    
    ghostbusters,    
    et,   
    blade_runner,    
    terminator
]

# Create users

harry_kane = User(email_address='harry@retro.com', password='password', first_name='Harry', last_name='Kane', dob='1993-07-28', mailing=True, pin=1234)
judy_dench = User(email_address='judy@retro.com', password='password1', first_name='Judy', last_name='Dench', dob='1934-12-09', mailing=True, pin=4567)
jimmy_carr = User(email_address='jimmy@retro.com', password='p@ssw0rd', first_name='Jimmy', last_name='Carr', dob='1972-11-15', mailing=True, pin=8912)

users = [
    jimmy_carr,
    judy_dench,
    harry_kane,
]

# Create card details

cards = [
    {'name_on_card': 'Harry Kane', 'card_number': '1234456712345678', 'expiry_date': '01/24', 'cvv': '123'},
    {'name_on_card': 'Judy Dench', 'card_number': '9874561298745612', 'expiry_date': '02/25', 'cvv': '456'},
    {'name_on_card': 'Jimmy Carr', 'card_number': '1478523614785236', 'expiry_date': '03/26', 'cvv': '789'},
]

# Create subscriptions

subscription_1 = Subscription(duration='1', price=4.99, sub_type='monthly')
subscription_2 = Subscription(duration='12', price=49.99, sub_type='yearly')

subscriptions = [
    subscription_1,
    subscription_2
]

# Create Tv Series

series = [
    {'title': 'Friends', 'release_year': 1994, 'age_rating': 'TV-PG', 'rating': 8.9},
    {'title': 'Cheers', 'release_year': 1982, 'age_rating': 'TV-PG', 'rating': 8.0},
    {'title': 'Frasier', 'release_year': 1993, 'age_rating': 'TV-PG', 'rating': 8.2},
    {'title': 'Married With Children', 'release_year': 1987, 'age_rating': 'TV-PG', 'rating': 8.1},
    {'title': 'Golden Girls', 'release_year': 1985, 'age_rating': 'TV-PG', 'rating': 8.2},
    {'title': 'Moonlighting', 'release_year': 1985, 'age_rating': 'TV-PG', 'rating': 7.6}
]

# Create Tv Series Seasons

seasons = [
    {"tv_series": "Friends", "release_year": 1994, "season_number": 1},
    {"tv_series": "Friends", "release_year": 1995, "season_number": 2},
    {"tv_series": "Friends", "release_year": 1996, "season_number": 3},
    {"tv_series": "Cheers", "release_year": 1982, "season_number": 1},
    {"tv_series": "Cheers", "release_year": 1983, "season_number": 2},
    {"tv_series": "Cheers", "release_year": 1984, "season_number": 3},
    {"tv_series": "Frasier", "release_year": 1993, "season_number": 1},
    {"tv_series": "Frasier", "release_year": 1994, "season_number": 2},
    {"tv_series": "Frasier", "release_year": 1995, "season_number": 3},
    {"tv_series": "Married With Children", "release_year": 1987, "season_number": 1},
    {"tv_series": "Married With Children", "release_year": 1988, "season_number": 2},
    {"tv_series": "Married With Children", "release_year": 1989, "season_number": 3},
    {"tv_series": "Golden Girls", "release_year": 1985, "season_number": 1},
    {"tv_series": "Golden Girls", "release_year": 1986, "season_number": 2},
    {"tv_series": "Golden Girls", "release_year": 1987, "season_number": 3},
    {"tv_series": "Moonlighting", "release_year": 1985, "season_number": 1},
    {"tv_series": "Moonlighting", "release_year": 1986, "season_number": 2},
    {"tv_series": "Moonlighting", "release_year": 1987, "season_number": 3},
]

# Create Tv Series Episodes

episodes = [
    {"tv_series": "Friends", "season": 1, "episode_number": 1, "title": "The One Where Monica Gets a Roommate", "release_year": 1994, "duration": "00:22:00"},
    {"tv_series": "Friends", "season": 1, "episode_number": 2, "title": "The One with the Sonogram at the End", "release_year": 1994, "duration": "00:22:00"},
    {"tv_series": "Friends", "season": 1, "episode_number": 3, "title": "The One with the Thumb", "release_year": 1994, "duration": "00:22:00"},

    {"tv_series": "Friends", "season": 2, "episode_number": 1, "title": "The One with Ross's New Girlfriend", "release_year": 1995, "duration": "00:22:00"},
    {"tv_series": "Friends", "season": 2, "episode_number": 2, "title": "The One with the Breast Milk", "release_year": 1995, "duration": "00:22:00"},
    {"tv_series": "Friends", "season": 2, "episode_number": 3, "title": "The One Where Heckles Dies", "release_year": 1995, "duration": "00:22:00"},

    {"tv_series": "Friends", "season": 3, "episode_number": 1, "title": "The One with the Princess Leia Fantasy", "release_year": 1996, "duration": "00:22:00"},
    {"tv_series": "Friends", "season": 3, "episode_number": 2, "title": "The One Where No One's Ready", "release_year": 1996, "duration": "00:22:00"},
    {"tv_series": "Friends", "season": 3, "episode_number": 3, "title": "The One with the Jam", "release_year": 1996, "duration": "00:22:00"},

    {"tv_series": "Cheers", "season": 1, "episode_number": 1, "title": "Give Me a Ring Sometime", "release_year": 1982, "duration": "00:24:03"},
    {"tv_series": "Cheers", "season": 1, "episode_number": 2, "title": "Sam's Women", "release_year": 1982, "duration": "00:24:14"},
    {"tv_series": "Cheers", "season": 1, "episode_number": 3, "title": "The Tortelli Tort", "release_year": 1982, "duration": "00:24:08"},

    {"tv_series": "Cheers", "season": 2, "episode_number": 1, "title": "Power Play", "release_year": 1983, "duration": "00:24:00"},
    {"tv_series": "Cheers", "season": 2, "episode_number": 2, "title": "Little Sister Don't Cha", "release_year": 1983, "duration": "00:24:13"},
    {"tv_series": "Cheers", "season": 2, "episode_number": 3, "title": "Personal Business", "release_year": 1983, "duration": "00:24:08"},

    {"tv_series": "Cheers", "season": 3, "episode_number": 1, "title": "Rebound: Part 1", "release_year": 1984, "duration": "00:24:02"},
    {"tv_series": "Cheers", "season": 3, "episode_number": 2, "title": "Rebound: Part 2", "release_year": 1984, "duration": "00:24:09"},
    {"tv_series": "Cheers", "season": 3, "episode_number": 3, "title": "I Call Your Name", "release_year": 1984, "duration": "00:24:09"},

    {"tv_series": "Frasier", "season": 1, "episode_number": 1, "title": "The Good Son", "release_year": 1993, "duration": "00:23:49"},
    {"tv_series": "Frasier", "season": 1, "episode_number": 2, "title": "Space Quest", "release_year": 1993, "duration": "00:22:51"},
    {"tv_series": "Frasier", "season": 1, "episode_number": 3, "title": "Dinner at Eight", "release_year": 1993, "duration": "00:22:49"},

    {"tv_series": "Frasier", "season": 2, "episode_number": 1, "title": "Slow Tango in South Seattle", "release_year": 1994, "duration": "00:23:36"},
    {"tv_series": "Frasier", "season": 2, "episode_number": 2, "title": "The Unkindest Cut of All", "release_year": 1994, "duration": "00:23:06"},
    {"tv_series": "Frasier", "season": 2, "episode_number": 3, "title": "The Matchmaker", "release_year": 1994, "duration": "00:22:45"},

    {"tv_series": "Frasier", "season": 3, "episode_number": 1, "title": "She's the Boss", "release_year": 1995, "duration": "00:23:04"},
    {"tv_series": "Frasier", "season": 3, "episode_number": 2, "title": "The Unnatural", "release_year": 1995, "duration": "00:22:58"},
    {"tv_series": "Frasier", "season": 3, "episode_number": 3, "title": "Frasier Grinch", "release_year": 1995, "duration": "00:22:54"},

    {"tv_series": "Married With Children", "season": 1, "episode_number": 1, "title": "Pilot", "release_year": 1987, "duration": "00:23:00"},
    {"tv_series": "Married With Children", "season": 1, "episode_number": 2, "title": "Thinnergy", "release_year": 1987, "duration": "00:23:00"},
    {"tv_series": "Married With Children", "season": 1, "episode_number": 3, "title": "But I Didn't Shoot the Deputy", "release_year": 1987, "duration": "00:23:00"},
    
    {"tv_series": "Married With Children", "season": 2, "episode_number": 1, "title": "Poppy's by the Tree (Part 1)", "release_year": 1987, "duration": "00:23:00"},
    {"tv_series": "Married With Children", "season": 2, "episode_number": 2, "title": "Poppy's by the Tree (Part 2)", "release_year": 1987, "duration": "00:23:00"},
    {"tv_series": "Married With Children", "season": 2, "episode_number": 3, "title": "If I Were a Rich Man", "release_year": 1987, "duration": "00:23:00"},
    
    {"tv_series": "Married With Children", "season": 3, "episode_number": 1, "title": "He Thought He Could", "release_year": 1988, "duration": "00:23:00"},
    {"tv_series": "Married With Children", "season": 3, "episode_number": 2, "title": "I'm Going to Sweatland", "release_year": 1988, "duration": "00:23:00"},
    {"tv_series": "Married With Children", "season": 3, "episode_number": 3, "title": "Poke High (aka Kelly Moves Out)", "release_year": 1988, "duration": "00:23:00"},

    {"tv_series": "Golden Girls", "season": 1, "episode_number": 1, "title": "The Engagement", "release_year": 1985, "duration": "00:24:09"},
    {"tv_series": "Golden Girls", "season": 1, "episode_number": 2, "title": "Guess Who's Coming to the Wedding?", "release_year": 1985, "duration": "00:24:09"},
    {"tv_series": "Golden Girls", "season": 1, "episode_number": 3, "title": "Rose the Prude", "release_year": 1985, "duration": "00:24:09"},

    {"tv_series": "Golden Girls", "season": 2, "episode_number": 1, "title": "End of the Curse", "release_year": 1986, "duration": "00:24:06"},
    {"tv_series": "Golden Girls", "season": 2, "episode_number": 2, "title": "Ladies of the Evening", "release_year": 1986, "duration": "00:24:06"},
    {"tv_series": "Golden Girls", "season": 2, "episode_number": 3, "title": "Take Him, He's Mine", "release_year": 1986, "duration": "00:24:06"},

    {"tv_series": "Golden Girls", "season": 3, "episode_number": 1, "title": "Old Friends", "release_year": 1987, "duration": "00:24:03"},
    {"tv_series": "Golden Girls", "season": 3, "episode_number": 2, "title": "One for the Money", "release_year": 1987, "duration": "00:24:03"},
    {"tv_series": "Golden Girls", "season": 3, "episode_number": 3, "title": "Bringing Up Baby", "release_year": 1987, "duration": "00:24:03"},

    {"tv_series": "Moonlighting", "season": 1, "episode_number": 1, "title": "Moonlighting (Pilot)", "release_year": 1985, "duration": "01:33:00"},
    {"tv_series": "Moonlighting", "season": 1, "episode_number": 2, "title": "Gunfight at the So-So Corral", "release_year": 1985, "duration": "00:48:00"},
    {"tv_series": "Moonlighting", "season": 1, "episode_number": 3, "title": "Read the Mind... See the Movie", "release_year": 1985, "duration": "00:48:00"},

    {"tv_series": "Moonlighting", "season": 2, "episode_number": 1, "title": "Brother, Can You Spare a Blonde?", "release_year": 1986, "duration": "00:48:00"},
    {"tv_series": "Moonlighting", "season": 2, "episode_number": 2, "title": "The Lady in the Iron Mask", "release_year": 1986, "duration": "00:48:00"},
    {"tv_series": "Moonlighting", "season": 2, "episode_number": 3, "title": "Money Talks... Maddie Walks", "release_year": 1986, "duration": "00:48:00"},

    {"tv_series": "Moonlighting", "season": 3, "episode_number": 1, "title": "The Son Also Rises", "release_year": 1987, "duration": "00:48:00"},
    {"tv_series": "Moonlighting", "season": 3, "episode_number": 2, "title": "The Man Who Cried Wife", "release_year": 1987, "duration": "00:48:00"},
    {"tv_series": "Moonlighting", "season": 3, "episode_number": 3, "title": "Symphony in Knocked Flat", "release_year": 1987, "duration": "00:48:00"}
]

# Add data to DB
# Add genre, actor, film, tv series, tv series seasons, user, subscriptions data to the database

with app.app_context():
    db.session.add_all(actors)
    db.session.add_all(genres)
    db.session.add_all(films)
    db.session.add_all(users)
    db.session.add_all(subscriptions)

    db.session.bulk_insert_mappings(TVSeries, series)
    db.session.commit()



    tv_series_models = dict(db.session.execute(db.select(TVSeries.title, TVSeries.id)).all())
    
    for season in seasons:
        if season['tv_series'] in tv_series_models.keys():
            season['tv_series_id'] = tv_series_models[season['tv_series']]
    
    db.session.bulk_insert_mappings(TVSeriesSeason, seasons)
    db.session.commit()
    

    # Get all users from the database
    users = User.query.all()

    # Loops through each user and updates their password with a hashed version
    for user in users:
        hashed_password = generate_password_hash(user.password)
        user.password = hashed_password
        db.session.commit()


    # Add user FK to card details
    users = User.query.all()

    for user in users:
        full_name = f"{user.first_name} {user.last_name}"
        for card in cards:
            if card['name_on_card'] == full_name:
                card['user_id'] = user.id
    
    db.session.bulk_insert_mappings(CardDetail, cards)
    db.session.commit()

    #Adding TV Series Episodes data to DB
    # Getting Season FK for Episode table

    tv_seasons = db.session.query(TVSeriesSeason.tv_series_id, TVSeriesSeason.season_number, TVSeriesSeason.id).all()

    # Creates tuple 'keys' to link the tv show to the corresponding season (1-3 for all was confusingthe last dictionary) 
    tv_seasons_models = {}
    for season in tv_seasons:
        key = (season.tv_series_id, season.season_number)
        tv_seasons_models[key] = season.id


    # Iterates over episodes and adds the TVSeriesSeason ID
    for episode in episodes:
        tv_series_key = episode['tv_series']
        season_number = episode['season']
        tv_series_id = tv_series_models.get(tv_series_key)
        season_key = (tv_series_id, season_number)
        season_id = tv_seasons_models.get(season_key)
        if season_id:
            episode['tv_series_season_id'] = season_id
            
    db.session.bulk_insert_mappings(TVSeriesEpisode, episodes)
    db.session.commit()


    # Create film_actor associations

    jurassic_park.actors.append(sam_neill)
    jurassic_park.actors.append(laura_dern)
    jurassic_park.actors.append(jeff_goldblum)
    gremlins.actors.append(zach_galligan)
    gremlins.actors.append(phoebe_cates)
    gremlins.actors.append(hoyt_axton)
    ghostbusters.actors.append(bill_murray)
    ghostbusters.actors.append(dan_aykroyd)
    ghostbusters.actors.append(sigourney_weaver)
    et.actors.append(henry_thomas)
    et.actors.append(drew_barrymore)
    et.actors.append(dee_wallace)
    blade_runner.actors.append(harrison_ford)
    blade_runner.actors.append(rutger_hauer)
    blade_runner.actors.append(sean_young)
    terminator.actors.append(arnold_schwarzenegger)
    terminator.actors.append(michael_biehn)
    terminator.actors.append(linda_hamilton)

    # Create film_genre associations

    jurassic_park.genres.append(science_fiction)
    jurassic_park.genres.append(adventure)
    jurassic_park.genres.append(thriller)
    gremlins.genres.append(comedy)
    gremlins.genres.append(horror)
    gremlins.genres.append(fantasy)
    ghostbusters.genres.append(comedy)
    ghostbusters.genres.append(fantasy)
    et.genres.append(science_fiction)
    et.genres.append(family)
    et.genres.append(adventure)
    blade_runner.genres.append(science_fiction)
    blade_runner.genres.append(thriller)
    terminator.genres.append(science_fiction)
    terminator.genres.append(action)

    # Create episode_actor and episode_genre associations

    episodes = TVSeriesEpisode.query.filter(TVSeriesEpisode.seasons.has(TVSeriesSeason.tv_series.has(title='Friends')))
    for episode in episodes:
        episode.actors.append(jennifer_aniston)
        episode.actors.append(lisa_kudrow)
        episode.actors.append(matt_le_blanc)
        episode.actors.append(jeff_goldblum)
        episode.genres.append(comedy)
        episode.genres.append(sitcom)
        episode.genres.append(romance)
    db.session.commit()

    episodes = TVSeriesEpisode.query.filter(TVSeriesEpisode.seasons.has(TVSeriesSeason.tv_series.has(title='Cheers')))
    for episode in episodes:
        episode.actors.append(kirstie_alley)
        episode.actors.append(ted_danson)
        episode.actors.append(rhea_perlman)
        episode.genres.append(drama)
        episode.genres.append(sitcom)
        episode.genres.append(comedy)
    db.session.commit()

    episodes = TVSeriesEpisode.query.filter(TVSeriesEpisode.seasons.has(TVSeriesSeason.tv_series.has(title='Frasier')))
    for episode in episodes:
        episode.actors.append(kelsey_grammer)
        episode.actors.append(jane_leeves)
        episode.actors.append(john_mahoney)
        episode.genres.append(family)
        episode.genres.append(sitcom)
        episode.genres.append(comedy)
    db.session.commit()

    episodes = TVSeriesEpisode.query.filter(TVSeriesEpisode.seasons.has(TVSeriesSeason.tv_series.has(title='Married With Children')))
    for episode in episodes:
        episode.actors.append(ed_oneill)
        episode.actors.append(katy_sagal)
        episode.actors.append(christina_applegate)
        episode.genres.append(family)
        episode.genres.append(sitcom)
        episode.genres.append(comedy)
    db.session.commit()

    episodes = TVSeriesEpisode.query.filter(TVSeriesEpisode.seasons.has(TVSeriesSeason.tv_series.has(title='Golden Girls')))
    for episode in episodes:
        episode.actors.append(bea_arthur)
        episode.actors.append(betty_white)
        episode.actors.append(rue_mclanahan)
        episode.genres.append(drama)
        episode.genres.append(sitcom)
        episode.genres.append(comedy)
    db.session.commit()

    episodes = TVSeriesEpisode.query.filter(TVSeriesEpisode.seasons.has(TVSeriesSeason.tv_series.has(title='Moonlighting')))
    for episode in episodes:
        episode.actors.append(cybill_shepherd)
        episode.actors.append(bruce_willis)
        episode.actors.append(allyce_beasley)
        episode.genres.append(drama)
        episode.genres.append(romance)
        episode.genres.append(mystery)
    db.session.commit()


    # Generating random login data for stats

    users = User.query.all()
    current_time = datetime.utcnow()

    login_entries = []

    for user in users:
        for _ in range(50):
            random_days = randint(0, 6) 
            random_time = current_time - timedelta(days=random_days)
            login = Login(user_id=user.id, timestamp=random_time)
            login_entries.append(login)

    sorted_entries = sorted(login_entries, key=lambda x: x.timestamp)  # Sort by timestamp before committing

    db.session.add_all(sorted_entries)
    db.session.commit()

    # Generating random film view counts for stats

    films = Film.query.all()
    current_time = datetime.now()

    all_view_times = []

    for film in films:
        num_views = randint(0, 100) 
        view_times = [current_time - timedelta(days=i) for i in range(num_views)]

        all_view_times.extend(view_times)

    sorted_view_times = sorted(all_view_times)

    for view_time in sorted_view_times:
        film_id = randint(1, len(films)) 
        film_view = FilmViews(film_id=film_id, timestamp=view_time)
        db.session.add(film_view)

    db.session.commit()

    # Generte retention entries

    fake = Faker()

    entries = []

    for _ in range(50):
        email_address = fake.email()

        types = ["create", "delete"]
        type = choice(types)

        end_date = datetime.now()
        start_date = end_date - timedelta(days=90) 
        timestamp = fake.date_time_between(start_date=start_date, end_date=end_date)

        retention_entry = Retention(type=type, email_address=email_address, timestamp=timestamp)
        entries.append(retention_entry)

    entries.sort(key=lambda x: x.timestamp)

    for entry in entries:
        db.session.add(entry)

    db.session.commit()



print('Database seeded successfully!')
