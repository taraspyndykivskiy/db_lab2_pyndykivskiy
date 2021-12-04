-- Cтовпчикова діаграма
select playerType, count(*) from game_plays_players group by playerType

-- Кругова діаграма
SELECT abbreviation, sum(away_goals) as goals from team_info join game on game.away_team_id=team_info.team_id
group by abbreviation

-- Графік залежності
SELECT game.home_goals, sum(game_skater_stats.shots) as home_overall_shots from game join game_skater_stats on game.game_id=game_skater_stats.game_id
group by game.home_goals
order by sum(game_skater_stats.shots) asc