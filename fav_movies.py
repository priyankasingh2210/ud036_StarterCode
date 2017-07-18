import media
import fresh_tomatoes


# Hindi movies instanaces
highway = media.Movie("Highway",
                      "In bondage she found freedom.",
                      "http://www.nadiadwalagrandson.com/sites/default/files/MovieImages/highway3.jpg",  # noqa
                      "https://www.youtube.com/watch?v=LSrDD52bx4A")
tamasha = media.Movie("Tamasha",
                      "A journey of someone who has lost his edge in trying"
                      "to follow socially acceptable conventions of society.",
                      "http://media.glamsham.com/download/poster/images/tamasha/03-tamasha.JPG",  # noqa
                      "https://www.youtube.com/watch?v=o-e5eWVCzx8")
dear_zindagi = media.Movie("Dear Zindagi",
                           "Happiness is all about finding comfort in life's imperfections.",  # noqa
                           "http://www.bollywoodlife.com/wp-content/uploads/2016/10/dear-zindagi.jpg",  # noqa
                           "https://www.youtube.com/watch?v=5DkO7ksXY8E")
hum_aapke_hain_kaun = media.Movie("Hum Aapke Hain Kaun",
                                  "A family drama involving one sweet love story.",  # noqa
                                  "https://upload.wikimedia.org/wikipedia/en/7/79/Hahk.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=45JY12a6zJA")  # noqa
zindagi_na_milegi_dobara = media.Movie("Zindagi Na Milegi Dobara",
                                       "Three friends decide to turn their fantasy vacation into reality after one of them becomes engaged.",  # noqa
                                       "http://www.impawards.com/intl/india/2011/posters/zindagi_na_milegi_dobara_ver3_xlg.jpg",  # noqa
                                       "https://www.youtube.com/watch?v=FJrpcDgC3zU")  # noqa
jab_we_met = media.Movie("Jab We Met",
                         "A depressed businessman finds his life"
                         "changing after he meets a care-free young woman.",
                         "http://media.glamsham.com/download/poster/images/jab_we_met/01.jpg",  # noqa
                         "https://www.youtube.com/watch?v=SJdVQh7HT4g")

# English movies instanaces
she_is_the_man = media.Movie("She's The Man",
                             "If you wanna chase your dream, sometimes you gotta break the rules.",  # noqa
                             "http://movieposters.2038.net/p/She-s-the-Man_2.jpg",  # noqa
                             "https://www.youtube.com/watch?v=D4OhwrMidSU")
eat_pray_love = media.Movie("Eat Pray Love",
                            "After a painful divorce, Liz takes off on a round-the-world journey to find herself.",  # noqa
                            "http://www.impawards.com/2010/posters/eat_pray_love_ver3.jpg",  # noqa
                            "https://www.youtube.com/watch?v=mjay5vgIwt4")
step_up = media.Movie("Step Up 2: The Streets",
                      "Romantic sparks occur between two dance students from different"  # noqa
                      "backgrounds at the Maryland School of the Arts",
                      "http://www.freemovieposters.net/posters/step_up_2_the_streets_2008_5087_poster.jpg",  # noqa
                      "https://www.youtube.com/watch?v=bL2wDI-O5YQ")
frozen = media.Movie("Frozen",
                     "story inspired by The Snow Queen",
                     "https://image.tmdb.org/t/p/original/jIjdFXKUNtdf1bwqMrhearpyjMj.jpg",  # noqa
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")
harry_potter = media.Movie("Harry Potter and the Sorcerer's Stone",
                           "Rescued from the outrageous neglect of"
                           "his aunt and uncle, a young boy with a great"
                           "destiny proves his worth while attending"
                           "Hogwarts School of Witchcraft and Wizardry.",
                           "http://www.impawards.com/2001/posters/harry_potter_and_the_sorcerers_stone_ver4.jpg",  # noqa
                           "https://www.youtube.com/watch?v=VyHV0BRtdxo")
troy = media.Movie("Troy",
                   "An adaptation of Homer's great epic, "
                   "the film follows the assault on Troy"
                   "by the united Greek forces and"
                   "chronicles the fates of the men involved",
                   "http://www.impawards.com/2004/posters/troy_ver7.jpg",
                   "https://www.youtube.com/watch?v=znTLzRJimeY")

# Favorite English Movies
english_movies = [she_is_the_man, eat_pray_love,
                  step_up, harry_potter, troy, frozen]

# Favorite Hindi Movies
hindi_movies = [highway, tamasha, dear_zindagi, jab_we_met,
                zindagi_na_milegi_dobara, hum_aapke_hain_kaun]

# calling open_movies_page to get all the list of fav movies into browser
fresh_tomatoes.open_movies_page(hindi_movies+english_movies)
