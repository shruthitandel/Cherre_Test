
--1. find the ten people who have visited the most sites
select personID, people.first_name || ' ' || people.last_name as Name, count(*) as Num_of_visits
from (select personId from visits group by  personId, siteId) as group_results 
left join people on people.id = group_results.personId
group by personId
order by Num_of_visits desc 
LIMIT 10


--2. list these people in descending order of the number of sites they've visited in a table called FrequentBrowsers
INSERT INTO frequent_browsers (person_id, num_sites_visited)
select personID, count(*) as num_sites_visited
from (select personId from visits group by  personId, siteId) as group_results 
left join people on people.id = group_results.personId
group by personId
order by num_sites_visited desc
LIMIT 10