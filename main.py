import psycopg2

username = 'taras_pyndykivskiy'
password = 'taras_pyndykivskiy'
database = 'second_lab'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT playerType, count(*) from game_plays_players group by playerType
'''

query_2='''
SELECT abbreviation, sum(away_goals) as goals from team_info join game on game.away_team_id=team_info.team_id
group by abbreviation
'''

query_3 = '''
SELECT game.home_goals, sum(game_skater_stats.shots) as home_overall_shots from game join game_skater_stats on game.game_id=game_skater_stats.game_id
group by game.home_goals
order by sum(game_skater_stats.shots) asc
'''

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with con:

    print("\nРезультат виконання першого запиту : \n")
    cur = con.cursor()
    cur.execute(query_1)
    for row in cur:
        print(row)

    print("\n\nРезультат виконання другого запиту : \n")
    cur.execute(query_2)
    for row in cur:
        print(row)

    print("\n\nРезультат виконання третього запиту : \n")
    cur.execute(query_3)
    for row in cur:
        print(row)
