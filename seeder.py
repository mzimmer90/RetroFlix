from application import db, Actor, Genre, Film, TVSeries, TVSeriesSeason, TVSeriesEpisode, User, CardDetail, Subscription
from application import app

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

genres = [
    action,    
    adventure,    
    comedy,    
    family,    
    fantasy,    
    horror,    
    science_fiction,    
    thriller
]


# Create films

jurassic_park = Film(title='Jurassic Park', release_year=1993, duration='02:07:00', age_rating='PG-13', rating=8.2)
gremlins = Film(title='Gremlins', release_year=1984, duration='01:46:00', age_rating='PG', rating=7.3)
ghostbusters = Film(title='Ghostbusters', release_year=1984, duration='01:45:00', age_rating='PG', rating=7.8)
et = Film(title='E.T. the Extra-Terrestrial', release_year=1982, duration='01:55:00', age_rating='PG', rating=7.9)
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


# Create tv series

friends = TVSeries(title='Friends', release_year=1994, age_rating='TV-PG', rating=8.9)
cheers = TVSeries(title='Cheers', release_year=1982, age_rating='TV-PG', rating=8.0)
frasier = TVSeries(title='Frasier', release_year=1993, age_rating='TV-PG', rating=8.2)
married_with_children = TVSeries(title='Married With Children', release_year=1987, age_rating='TV-PG', rating=8.1)
golden_girls = TVSeries(title='The Golden Girls', release_year=1985, age_rating='TV-PG', rating=8.2)
moonlighting = TVSeries(title='Moonlighting', release_year=1985, age_rating='TV-PG', rating=7.6)

tv_series = [
    friends,
    cheers,
    frasier,
    married_with_children,
    golden_girls,
    moonlighting
]




# Create tv series seasons

friends_s_1 = TVSeriesSeason(tv_series_id=friends.id, release_year=1994, season_number=1)
friends_s_2 = TVSeriesSeason(tv_series_id=friends.id, release_year=1995, season_number=2)
friends_s_3 = TVSeriesSeason(tv_series_id=friends.id, release_year=1996, season_number=3)

cheers_s_1 = TVSeriesSeason(tv_series_id=cheers.id, release_year=1982, season_number=1)
cheers_s_2 = TVSeriesSeason(tv_series_id=cheers.id, release_year=1983, season_number=2)
cheers_s_3 = TVSeriesSeason(tv_series_id=cheers.id, release_year=1984, season_number=3)

frasier_s_1 = TVSeriesSeason(tv_series_id=frasier.id, release_year=1993, season_number=1)
frasier_s_2 = TVSeriesSeason(tv_series_id=frasier.id, release_year=1994, season_number=2)
frasier_s_3 = TVSeriesSeason(tv_series_id=frasier.id, release_year=1995, season_number=3) 

married_with_children_s_1 = TVSeriesSeason(tv_series_id=married_with_children.id, release_year=1987, season_number=1)
married_with_children_s_2 = TVSeriesSeason(tv_series_id=married_with_children.id, release_year=1988, season_number=2)
married_with_children_s_3 = TVSeriesSeason(tv_series_id=married_with_children.id, release_year=1989, season_number=3)

golden_girls_s_1 = TVSeriesSeason(tv_series_id=golden_girls.id, release_year=1985, season_number=1)
golden_girls_s_2 = TVSeriesSeason(tv_series_id=golden_girls.id, release_year=1986, season_number=3)
golden_girls_s_3 = TVSeriesSeason(tv_series_id=golden_girls.id, release_year=1987, season_number=3)

moonlighting_s_1 = TVSeriesSeason(tv_series_id=moonlighting.id, release_year=1985, season_number=1)
moonlighting_s_2 = TVSeriesSeason(tv_series_id=moonlighting.id, release_year=1986, season_number=2)
moonlighting_s_3 = TVSeriesSeason(tv_series_id=moonlighting.id, release_year=1987, season_number=3)


tv_series_seasons = [
    friends_s_1,
    friends_s_2,
    friends_s_3,
    cheers_s_1,
    cheers_s_2,
    cheers_s_3,
    frasier_s_1,
    frasier_s_2,
    frasier_s_3,
    married_with_children_s_1,
    married_with_children_s_2,
    married_with_children_s_3,
    golden_girls_s_1,
    golden_girls_s_2,
    golden_girls_s_3,
    moonlighting_s_1,
    moonlighting_s_2,
    moonlighting_s_3
]

# Create tv series episodes

friends_s_1_ep_1 = TVSeriesEpisode(tv_series_season_id=friends_s_1.id, episode_number=1, title='The One Where Monica Gets a Roommate', release_year=1994, duration='00:22:00')
friends_s_1_ep_2 = TVSeriesEpisode(tv_series_season_id=friends_s_1.id, episode_number=2, title='The One with the Sonogram at the End', release_year=1994, duration='00:22:00')
friends_s_1_ep_3 = TVSeriesEpisode(tv_series_season_id=friends_s_1.id, episode_number=3, title='The One with the Thumb', release_year=1994, duration='00:22:00')

friends_s_2_ep_1 = TVSeriesEpisode(tv_series_season_id=friends_s_2.id, episode_number=1, title='The One with Ross\'s New Girlfriend', release_year=1995, duration='00:22:00')
friends_s_2_ep_2 = TVSeriesEpisode(tv_series_season_id=friends_s_2.id, episode_number=2, title='The One with the Breast Milk', release_year=1995, duration='00:22:00')
friends_s_2_ep_3 = TVSeriesEpisode(tv_series_season_id=friends_s_2.id, episode_number=3, title='The One Where Heckles Dies', release_year=1995, duration='00:22:00')

friends_s_3_ep_1 = TVSeriesEpisode(tv_series_season_id=friends_s_3.id, episode_number=1, title='The One with the Princess Leia Fantasy', release_year=1996, duration='00:22:00')
friends_s_3_ep_2 = TVSeriesEpisode(tv_series_season_id=friends_s_3.id, episode_number=2, title='The One Where No One\'s Ready', release_year=1996, duration='00:22:00')
friends_s_3_ep_3 = TVSeriesEpisode(tv_series_season_id=friends_s_3.id, episode_number=3, title='The One with the Jam', release_year=1996, duration='00:22:00')

cheers_s_1_ep_1 = TVSeriesEpisode(tv_series_season_id=cheers_s_1.id, episode_number=1, title='Give Me a Ring Sometime', release_year=1982, duration='00:24:03')
cheers_s_1_ep_2 = TVSeriesEpisode(tv_series_season_id=cheers_s_1.id, episode_number=2, title='Sam\'s Women', release_year=1982, duration='00:24:14')
cheers_s_1_ep_3 = TVSeriesEpisode(tv_series_season_id=cheers_s_1.id, episode_number=3, title='The Tortelli Tort', release_year=1982, duration='00:24:08')

cheers_s_2_ep_1 = TVSeriesEpisode(tv_series_season_id=cheers_s_2.id, episode_number=1, title='Power Play', release_year=1983, duration='00:24:00')
cheers_s_2_ep_2 = TVSeriesEpisode(tv_series_season_id=cheers_s_2.id, episode_number=2, title='Little Sister Don\'t Cha', release_year=1983, duration='00:24:13')
cheers_s_2_ep_3 = TVSeriesEpisode(tv_series_season_id=cheers_s_2.id, episode_number=3, title='Personal Business', release_year=1983, duration='00:24:08')

cheers_s_3_ep_1 = TVSeriesEpisode(tv_series_season_id=cheers_s_3.id, episode_number=1, title='Rebound: Part 1', release_year=1984, duration='00:24:02')
cheers_s_3_ep_2 = TVSeriesEpisode(tv_series_season_id=cheers_s_3.id, episode_number=2, title='Rebound: Part 2', release_year=1984, duration='00:24:09')
cheers_s_3_ep_3 = TVSeriesEpisode(tv_series_season_id=cheers_s_3.id, episode_number=3, title='I Call Your Name', release_year=1984, duration='00:24:09')

frasier_s_1_ep_1 = TVSeriesEpisode(tv_series_season_id=frasier_s_1.id, episode_number=1, title='The Good Son', release_year=1993, duration='00:23:49')
frasier_s_1_ep_2 = TVSeriesEpisode(tv_series_season_id=frasier_s_1.id, episode_number=2, title='Space Quest', release_year=1993, duration='00:22:51')
frasier_s_1_ep_3 = TVSeriesEpisode(tv_series_season_id=frasier_s_1.id, episode_number=3, title='Dinner at Eight', release_year=1993, duration='00:22:49')

frasier_s_2_ep_1 = TVSeriesEpisode(tv_series_season_id=frasier_s_2.id, episode_number=1, title='Slow Tango in South Seattle', release_year=1994, duration='00:23:36')
frasier_s_2_ep_2 = TVSeriesEpisode(tv_series_season_id=frasier_s_2.id, episode_number=2, title='The Unkindest Cut of All', release_year=1994, duration='00:23:06')
frasier_s_2_ep_3 = TVSeriesEpisode(tv_series_season_id=frasier_s_2.id, episode_number=3, title='The Matchmaker', release_year=1994, duration='00:22:45')

frasier_s_3_ep_1 = TVSeriesEpisode(tv_series_season_id=frasier_s_3.id, episode_number=1, title='She\'s the Boss', release_year=1995, duration='00:23:04')
frasier_s_3_ep_2 = TVSeriesEpisode(tv_series_season_id=frasier_s_3.id, episode_number=2, title='The Unnatural', release_year=1995, duration='00:22:58')
frasier_s_3_ep_3 = TVSeriesEpisode(tv_series_season_id=frasier_s_3.id, episode_number=3, title='Frasier Grinch', release_year=1995, duration='00:22:54')

married_with_children_s_1_ep_1 = TVSeriesEpisode(tv_series_season_id=married_with_children_s_1.id, episode_number=1, title='Pilot', release_year=1987, duration='00:23:00')
married_with_children_s_1_ep_2 = TVSeriesEpisode(tv_series_season_id=married_with_children_s_1.id, episode_number=2, title='Thinnergy', release_year=1987, duration='00:23:00')
married_with_children_s_1_ep_3 = TVSeriesEpisode(tv_series_season_id=married_with_children_s_1.id, episode_number=3, title='But I Didn\'t Shoot the Deputy', release_year=1987, duration='00:23:00')

married_with_children_s_2_ep_1 = TVSeriesEpisode(tv_series_season_id=married_with_children_s_2.id, episode_number=1, title='Poppy\'s by the Tree (Part 1)', release_year=1987, duration='00:23:00')
married_with_children_s_2_ep_2 = TVSeriesEpisode(tv_series_season_id=married_with_children_s_2.id, episode_number=2, title='Poppy\'s by the Tree (Part 2)', release_year=1987, duration='00:23:00')
married_with_children_s_2_ep_3 = TVSeriesEpisode(tv_series_season_id=married_with_children_s_2.id, episode_number=3, title='If I Were a Rich Man', release_year=1987, duration='00:23:00')

married_with_children_s_3_ep_1 = TVSeriesEpisode(tv_series_season_id=married_with_children_s_3.id, episode_number=1, title='He Thought He Could', release_year=1988, duration='00:23:00')
married_with_children_s_3_ep_2 = TVSeriesEpisode(tv_series_season_id=married_with_children_s_3.id, episode_number=2, title='I\'m Going to Sweatland', release_year=1988, duration='00:23:00')
married_with_children_s_3_ep_3 = TVSeriesEpisode(tv_series_season_id=married_with_children_s_3.id, episode_number=3, title='Poke High (aka Kelly Moves Out)', release_year=1988, duration='00:23:00')

golden_girls_s_1_ep_1 = TVSeriesEpisode(tv_series_season_id=golden_girls_s_1.id, episode_number=1, title='The Engagement', release_year=1985, duration='00:24:09')
golden_girls_s_1_ep_2 = TVSeriesEpisode(tv_series_season_id=golden_girls_s_1.id, episode_number=2, title='Guess Who\'s Coming to the Wedding?', release_year=1985, duration='00:24:09')
golden_girls_s_1_ep_3 = TVSeriesEpisode(tv_series_season_id=golden_girls_s_1.id, episode_number=3, title='Rose the Prude', release_year=1985, duration='00:24:09')

golden_girls_s_2_ep_1 = TVSeriesEpisode(tv_series_season_id=golden_girls_s_2.id, episode_number=1, title='End of the Curse', release_year=1986, duration='00:24:06')
golden_girls_s_2_ep_2 = TVSeriesEpisode(tv_series_season_id=golden_girls_s_2.id, episode_number=2, title='Ladies of the Evening', release_year=1986, duration='00:24:06')
golden_girls_s_2_ep_3 = TVSeriesEpisode(tv_series_season_id=golden_girls_s_2.id, episode_number=3, title='Take Him, He\'s Mine', release_year=1986, duration='00:24:06')

golden_girls_s_3_ep_1 = TVSeriesEpisode(tv_series_season_id=golden_girls_s_3.id, episode_number=1, title='Old Friends', release_year=1987, duration='00:24:03')
golden_girls_s_3_ep_2 = TVSeriesEpisode(tv_series_season_id=golden_girls_s_3.id, episode_number=2, title='One for the Money', release_year=1987, duration='00:24:03')
golden_girls_s_3_ep_3 = TVSeriesEpisode(tv_series_season_id=golden_girls_s_3.id, episode_number=3, title='Bringing Up Baby', release_year=1987, duration='00:24:03')

moonlighting_s_1_ep_1 = TVSeriesEpisode(tv_series_season_id=moonlighting_s_1.id, episode_number=1, title='Moonlighting (Pilot)', release_year=1985, duration='01:33:00')
moonlighting_s_1_ep_2 = TVSeriesEpisode(tv_series_season_id=moonlighting_s_1.id, episode_number=2, title='Gunfight at the So-So Corral', release_year=1985, duration='00:48:00')
moonlighting_s_1_ep_3 = TVSeriesEpisode(tv_series_season_id=moonlighting_s_1.id, episode_number=3, title='Read the Mind... See the Movie', release_year=1985, duration='00:48:00')

moonlighting_s_2_ep_1 = TVSeriesEpisode(tv_series_season_id=moonlighting_s_2.id, episode_number=1, title='Brother, Can You Spare a Blonde?', release_year=1986, duration='00:48:00')
moonlighting_s_2_ep_2 = TVSeriesEpisode(tv_series_season_id=moonlighting_s_2.id, episode_number=2, title='The Lady in the Iron Mask', release_year=1986, duration='00:48:00')
moonlighting_s_2_ep_3 = TVSeriesEpisode(tv_series_season_id=moonlighting_s_2.id, episode_number=3, title='Money Talks... Maddie Walks', release_year=1986, duration='00:48:00')

moonlighting_s_3_ep_1 = TVSeriesEpisode(tv_series_season_id=moonlighting_s_3.id, episode_number=1, title='The Son Also Rises', release_year=1987, duration='00:48:00')
moonlighting_s_3_ep_2 = TVSeriesEpisode(tv_series_season_id=moonlighting_s_3.id, episode_number=2, title='The Man Who Cried Wife', release_year=1987, duration='00:48:00')
moonlighting_s_3_ep_3 = TVSeriesEpisode(tv_series_season_id=moonlighting_s_3.id, episode_number=3, title='Symphony in Knocked Flat', release_year=1987, duration='00:48:00')

tv_series_episodes = [
    friends_s_1_ep_1,
    friends_s_1_ep_2,
    friends_s_1_ep_3,
    friends_s_2_ep_1,
    friends_s_2_ep_2,
    friends_s_2_ep_3,
    friends_s_3_ep_1,
    friends_s_3_ep_2,
    friends_s_3_ep_3,
    cheers_s_1_ep_1,
    cheers_s_1_ep_2,
    cheers_s_1_ep_3,
    cheers_s_2_ep_1,
    cheers_s_2_ep_2,
    cheers_s_2_ep_3,
    cheers_s_3_ep_1,
    cheers_s_3_ep_2,
    cheers_s_3_ep_3,
    frasier_s_1_ep_1,
    frasier_s_1_ep_2,
    frasier_s_1_ep_3,
    frasier_s_2_ep_1,
    frasier_s_2_ep_2,
    frasier_s_2_ep_3,
    frasier_s_3_ep_1,
    frasier_s_3_ep_2,
    frasier_s_3_ep_3,
    married_with_children_s_1_ep_1,
    married_with_children_s_1_ep_2,
    married_with_children_s_1_ep_3,
    married_with_children_s_2_ep_1,
    married_with_children_s_2_ep_2,
    married_with_children_s_2_ep_3,
    married_with_children_s_3_ep_1,
    married_with_children_s_3_ep_2,
    married_with_children_s_3_ep_3,
    golden_girls_s_1_ep_1,
    golden_girls_s_1_ep_2,
    golden_girls_s_1_ep_3,
    golden_girls_s_2_ep_1,
    golden_girls_s_2_ep_2,
    golden_girls_s_2_ep_3,
    golden_girls_s_3_ep_1,
    golden_girls_s_3_ep_2,
    golden_girls_s_3_ep_3,
    moonlighting_s_1_ep_1,
    moonlighting_s_1_ep_2,
    moonlighting_s_1_ep_3,
    moonlighting_s_2_ep_1,
    moonlighting_s_2_ep_2, 
    moonlighting_s_2_ep_3,
    moonlighting_s_3_ep_1,
    moonlighting_s_3_ep_2,
    moonlighting_s_3_ep_3
]

# Create users

harry_kane = User(email_address='harry@retro.com', _password='password', first_name='Harry', last_name='Kane', dob='1993-07-28', mailing=True, creation_date='2023-04-27', last_login='2023-04-27', pin=1234)
judy_dench = User(email_address='judy@retro.com', _password='password', first_name='Judy', last_name='Dench', dob='1934-12-09', mailing=True, creation_date='2023-04-27', last_login='2023-04-27', pin=4567)
jimmy_carr = User(email_address='jimmy@retro.com', _password='password', first_name='Jimmy', last_name='Carr', dob='1972-11-15', mailing=True, creation_date='2023-04-27', last_login='2023-04-27', pin=8912)

users = [
    harry_kane,
    judy_dench,
    jimmy_carr
]

# Create card details

# Create subscriptions

subscription_1 = Subscription(duration='rolling', price=4.99, sub_type='Monthly')
subscription_2 = Subscription(duration='12 months', price=49.99, sub_type='Yearly')

subscriptions = [
    subscription_1,
    subscription_2
] 

# Add genre, actor, film, tv series, tv series seasons user, subscriptions data to the database


with app.app_context():
    db.session.add_all(actors)
    db.session.add_all(genres)
    db.session.add_all(films)
    db.session.add_all(tv_series)
    db.session.add_all(tv_series_seasons)
    db.session.add_all(tv_series_episodes)
    db.session.add_all(users)
    db.session.add_all(subscriptions)
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

    # Create episode_actor associations


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

    # Create episode_genre associations



    db.session.commit()


print('Database seeded successfully!')
