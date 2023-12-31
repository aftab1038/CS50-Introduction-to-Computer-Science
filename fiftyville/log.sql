-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports
WHERE street = "Humphrey Street" AND year = "2021" AND month = "7" AND day = "28";
-- information :
-- 1. Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- 2. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.
-- 3. Littering took place at 16:36. No known witnesses.

-- using bakery
SELECT transcript FROM interviews
WHERE transcript LIKE "%bakery%" AND year = "2021" AND month = "7" AND day = "28";
-- Information from this :
-- 1. thief get into a car in the bakery parking lot and drive away
-- 2. earlier morning the theif was seen in the ATM on Leggett Street and withdrawing some money.
-- 3. Before leaving bakery he (theif) called someone and talked for less than a minute.

-- As theft took at 10:15. So names of people who leave the bakery parking lot in between 10:15 to 10:20.
SELECT name FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE year = "2021" AND month = "7" AND day = "28" AND hour = "10" AND minute >= "15" AND minute <= "20" AND activity = "exit";
-- First Suspects : Vanessa, Bruce, Barry, Luca, Sofia

-- Theif was seen in the ATM on Leggett Street and withdrawing some money
SELECT name FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE year = "2021" AND month = "7" AND day = "28" AND atm_transactions.atm_location = "Leggett Street" AND atm_transactions.transaction_type = "withdraw";
-- 2nd Suspects : Bruce, Diana, Brooke, Kenny, Iman, Luca, Taylor, Benista
-- Common Suspects : Bruce, luca.

-- From interview : Before leaving bakery theif called someone and talked for less than a minute.
SELECT name FROM people
JOIN phone_calls on people.phone_number = phone_calls.caller
WHERE year = "2021" AND month = "7" AND day = "28" AND phone_calls.duration < "60";
-- 3rd Suspects Sofia, Kelsey, Bruce, Kelsey, Taylor, Diana, Carina, Kenny, Benista
-- Common Suspects : Bruce
-- So Theif is bruce

-- What city the thief escaped to.
SELECT * FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE people.name = "Bruce";
-- the passport number of theif (Bruce) is 5773159633
-- And flight_id = 36

-- So the place he (Bruce) escaped is:
SELECT city FROM airports
JOIN flights ON airports.id = flights.destination_airport_id
WHERE flights.id = "36";
-- place Bruce Escaped is New York City

-- who the thief’s accomplice is who helped them escape
SELECT phone_number FROM people
WHERE name = "Bruce";
-- phone number of brue is : (367) 555-5533

-- finding phone number of thief’s accomplice is who helped them escape using theif bruce phone number
SELECT receiver FROM phone_calls
WHERE  caller = "(367) 555-5533" AND year = "2021" AND month = "7" AND day = "28" AND duration < "60";
-- Receiver phone number (thief’s accomplice) : (375) 555-8161

-- finding name of thief’s accomplice using his or her phone number : (375) 555-8161
SELECT name FROM people
WHERE phone_number = "(375) 555-8161";
-- Name of thief’s accomplice  is Robin
