-- Write a script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT g.`genre_id`, s.`title`
  FROM `tv_shows` AS s
       RIGHT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;