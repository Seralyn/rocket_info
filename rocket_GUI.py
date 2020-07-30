# import sys
# import os
import datetime
from tkinter import *
import tkinter.messagebox

root = Tk()
root.configure()
root.geometry("1350x800")
root.title("Working Title: SRP")

# *** Adds Icon to window ***
# works in windows, but not on Mac...why?
root.iconbitmap("rocket_icon 512.ico")

# *** Rocket Info Dictionary ***
rocketDictionary = {
    'Saturn V': {
        "Name": "Saturn V",
        "Agency": "NASA - National Aeronautics & Space Administration",
        "Payload Capacity to LEO": "140,000kg (310,000 lbs)",
        "Height": "110.6m (363ft)",
        "Diameter": "10.1m (33ft)",
        "Mass": "2,970,000 kg",
        "Years in Operation": "1967-1973",
        "Country": "USA",
        "Operational Status": "Retired",
        "Number of Stages": "2-3",
        "Additional Information":
            '''
            Saturn V was an American super heavy-lift launch vehicle 
            certified for human-rating used by NASA between 1967 and 
            1973. It consisted of three stages, each fueled by liquid 
            propellants. It was developed to support the Apollo program 
            for human exploration of the Moon and was later used to 
            launch Skylab, the first American space station.
    
            The Saturn V was launched 13 times from Kennedy Space Center 
            with no loss of crew or payload. As of 2020, the Saturn V 
            remains the tallest, heaviest, and most powerful (highest 
            total impulse) rocket ever brought to operational status, 
            and holds records for the heaviest payload launched and 
            largest payload capacity to low Earth orbit (LEO) of 
            310,000 lb (140,000 kg), which included the third stage 
            and unburned propellant needed to send the Apollo command 
            and service module and Lunar Module to the Moon.
    
            As the largest production model of the Saturn family of 
            rockets, the Saturn V was designed under the direction of 
            Wernher von Braun at the Marshall Space Flight Center in 
            Huntsville, Alabama, with Boeing, North American Aviation, 
            Douglas Aircraft Company, and IBM as the lead contractors.
    
            To date, the Saturn V remains the only launch vehicle to carry 
            humans beyond low Earth orbit. A total of 15 flight-capable 
            vehicles were built, but only 13 were flown. An additional 
            three vehicles were built for ground testing purposes. A total 
            of 24 astronauts were launched to the Moon in the four years 
            spanning December 1968 through December 1972.
            '''
    },
    'Soyuz': {
        "Name": "Soyuz",
        "Agency": "Roscosmos",
        "Payload Capacity to LEO": "6,450 kilograms (14,220 lbs)",
        "Height": "45.6m (150 ft)",
        "Diameter": "10.3m (34ft)",
        "Mass": "308,000 kg",
        "Years in Operation": "1966-present",
        "Country": "Russia",
        "Operational Status": "Active",
        "Number of Stages": "3",
        "Additional Information":
            '''
            Soyuz is a series of spacecraft designed for the Soviet space 
            program by the Korolev Design Bureau (now RKK Energia) in the
            1960s that remains in service today, having made more than 140 
            flights. The Soyuz succeeded the Voskhod spacecraft and was 
            originally built as part of the Soviet crewed lunar programs. 
            The Soyuz spacecraft is launched on a Soyuz rocket, the most 
            reliable launch vehicle in the world to date. The Soyuz 
            rocket design is based on the Vostok launcher, which in turn was 
            based on the 8K74 or R-7A Semyorka, a Soviet intercontinental 
            ballistic missile. All Soyuz spacecraft are launched from the 
            Baikonur Cosmodrome in Kazakhstan. After the retirement of the 
            Space Shuttle in 2011, the Soyuz served as the only means for 
            Americans to make crewed space flights until the first flight 
            of VSS Unity in 2018, and the only means for Americans to reach 
            the International Space Station until the first flight of Dragon 
            2 Crew variant on May 30, 2020. The Soyuz is heavily used in 
            the ISS program.
    
            The first Soyuz flight was uncrewed and started on November 28, 
            1966. The first Soyuz mission with a crew, Soyuz 1, launched on 
            23 April 1967 but ended with a crash due to a parachute failure, 
            killing cosmonaut Vladimir Komarov. The following flight was 
            uncrewed. Soyuz 3, launched on October 26, 1968, became the 
            program's first successful crewed mission. The only other flight 
            to suffer a fatal accident, Soyuz 11, killed its crew of three 
            when the cabin depressurized prematurely just before reentry. 
            These were the only humans to date to have died above the Kármán 
            line. Despite these early incidents, Soyuz is widely considered 
            the world's safest, most cost-effective human spaceflight vehicle, 
            established by its unparalleled length of operational history. 
            Soyuz spacecraft were used to carry cosmonauts to and from Salyut 
            and later Mir Soviet space stations, and are now used for transport 
            to and from the International Space Station (ISS). At least one Soyuz 
            spacecraft is docked to ISS at all times for use as an escape craft 
            in the event of an emergency. The spacecraft is intended to be 
            replaced by the six-person Orel spacecraft.
            '''
    },

    "Delta III": {
        "Name": "Delta III",
        "Agency": "Boeing & MHI - Mitsubishi Heavy Industries",
        "Payload Capacity to LEO": "8,290 kg (18,280 lbs)",
        "Height": "35m (115ft)",
        "Diameter": "4m (13ft)",
        "Mass": "301,450 kg",
        "Years in Operation": "1998-2000",
        "Country": "USA",
        "Operational Status": "Retired",
        "Number of Stages": "2",
        "Additional Information":
            '''
            The Delta III rocket was an expendable launch vehicle made by 
            Boeing. The first Delta III launch was on August 26, 1998. Of 
            its three flights, the first two were failures, and the third, 
            though declared successful, reached the low end of its targeted 
            orbit range and carried only a dummy (inert) payload. The Delta 
            III could deliver up to 8,400 pounds (3,800 kilograms) to 
            geostationary transfer orbit, twice the payload of its 
            predecessor, the Delta II. Under the 4-digit designation system 
            from earlier Delta rockets, the Delta III is classified as the 
            Delta 8930.
    
            Like the Delta II, the first stage of the Delta III burned kerosene 
            and liquid oxygen and was powered by one Rocketdyne RS-27A main 
            engine with two vernier engines for roll control. While the 
            propellant load and gross mass of the stage were nearly identical 
            to the Delta II, the diameter of the kerosene tank was increased 
            from 2.4 meters to 4 meters. This reduced the overall length of 
            the vehicle and allowed the Delta III to use the same launch 
            facilities as the Delta II with only minor modifications. First 
            stage thrust was augmented by nine GEM-46 solid rocket boosters, 
            sometimes referred to as GEM LDXL (Large Diameter Extended Length). 
            These were 14.7 meters in length, 1.2 m (46 inches) in diameter, 
            and had a mass of 19 metric tons each, about 6 metric tons more than 
            the Delta II's standard GEM-40 motors. Six were ignited on the launch 
            pad, while the remaining three were ignited just before burnout and 
            separation of the ground-lit boosters. To maintain steering authority, 
            three of the boosters had vectoring nozzles. GEM-46 boosters would 
            later find use on the Delta II, leading to the Delta II Heavy.
            '''
    },

    "Ariane 62": {
        "Name": "Ariane 62",
        "Agency": "ArianeGroup",
        "Payload Capacity to LEO": "10,350 kg (22,817 lbs)",
        "Height": "63m (207ft)",
        "Diameter": "5.4m (18ft)",
        "Mass": "530,000–860,000 kg",
        "Years in Operation": "2021~",
        "Country": "France(EU)",
        "Operational Status": "In Development",
        "Number of Stages": "2",
        "Additional Information":
            '''
            Ariane 6 is a launch vehicle developed and manufactured by 
            ArianeGroup under the authority of the European Space Agency 
            (ESA), with a first test flight scheduled for 2020 or, now 
            more likely, 2021. When development is completed, it will 
            become the newest member in the Ariane launch vehicle family. 
            The final design was selected in December 2014, favoring a 
            liquid-fuelled core with large solid rocket boosters over the 
            initial solid-fuel rocket design. The motivation for 
            Ariane 6 development was to replace Ariane 5 at half the cost, 
            and allow double the number of launches each year.
            
            Ariane 6 was initially conceived in the early 2010s as a 
            replacement launch vehicle for Ariane 5, and a number of 
            concepts and high-level designs were suggested and proposed 
            during 2012–2015. Funding from several European governments 
            was secured by early 2016, and contracts were signed to begin 
            detailed design and the build of test articles. While in 2019, 
            the maiden orbital flight had been planned for 2020, by May 
            2020, the planned initial launch date had been delayed until 2021.
            '''
    },
    "Tronador II": {
        "Name": "Tronador II",
        "Agency": "CNAE - Comisión Nacional de Actividades Espaciales",
        "Payload Capacity to LEO": "250 kg to Polar",
        "Height": "28 m (92 ft)",
        "Diameter": "2.5 m (8 ft 2 in)",
        "Mass": "67,000 kg (148,000 lb) (including propellant)",
        "Years in Operation": "2020(slated)~",
        "Country": "Argentina",
        "Operational Status": "Under Development",
        "Number of Stages": "3",
        "Additional Information":
            '''
            Tronador (Spanish for Thunderer) is a series of Argentine 
            rockets, including the Tronador I and Tronador II vehicles, 
            to develop a liquid-propellant rocket expendable launch 
            system called ISCUL (Inyector Satelital de Cargas Utiles 
            Ligeras, Light Useful Payloads Satellite Launcher).
    
            The Tronador I is an unguided liquid-fueled rocket[3] used 
            for sub-orbital spaceflight test flights. Its development 
            led to the larger VEx test rocket, testing technologies 
            needed for the Tronador II, which has a guidance system 
            and would be capable of reaching low Earth orbit. 
            Development of the satellite launch vehicle has cost more 
            than 600 million dollars over several years.
            '''
    },
    "VLS-1": {
        "Name": "VLS-1",
        "Agency": "AEB - Agência Espacial Brasileira",
        "Payload Capacity to LEO": "380 kg (830 lb)",
        "Height": "19.5 m (63.9 ft)",
        "Diameter": "1.01 m (3.31 ft)",
        "Mass": "50,700 kg (111,700 lb)",
        "Years in Operation": "N/A",
        "Country": "Brazil",
        "Operational Status": "Canceled",
        "Number of Stages": "3",
        "Additional Information":
            '''
            The VLS-1 (Portuguese: Veículo Lançador de Satélites)
            was the Brazilian Space Agency's main satellite launch 
            vehicle. The launch vehicle was to be capable of 
            launching satellites into orbit. The launch site was 
            located at the Alcântara Launch Center due to its 
            proximity to the equator.
    
            Associated vehicles include the Sonda I, Sonda II, 
            Sonda III and Sonda IV, the VS-30, VS-40 and VSB-30.
    
            The VLS was cancelled after decades of development 
            and high expenditures with poor results and a failed 
            association with Ukraine that slowed the program 
            for years.
    
            VLS-1 development started in 1984, after the first 
            launch of the Sonda IV rocket. To date, three 
            prototypes have been built and two launches attempted, 
            departing from the Alcântara Launch Center. During 
            the V1 and V2 prototype launches (VLS-1 V1 and VLS-1 V2) 
            technical problems prevented mission success, but 
            allowed the testing of several vehicle components. 
            The V3 prototype exploded on the launch pad on 22 
            August 2003, two days before its intended launch date. 
            The 2003 Alcântara VLS accident caused a considerable 
            setback to the Brazilian space program. The V4 
            prototype was expected to be launched in 2016.
            '''
    },
    "VLM": {
        "Name": "VLM",
        "Agency": "AEB - Agência Espacial Brasileira",
        "Payload Capacity to LEO": "150 kg (330 lb)",
        "Height": "19.6 m (64 ft)",
        "Diameter": "1.45 m (4 ft 9 in)",
        "Mass": "28,000 kg (62,000 lb)",
        "Years in Operation": "N/A",
        "Country": "Brazil",
        "Operational Status": "In Development",
        "Number of Stages": "3",
        "Additional Information":
            '''
            The VLM (Veículo Lançador de Microssatélites) is a 
            proposed three-stage satellite launcher being developed 
            by the Brazilian General Command for Aerospace Technology 
            in collaboration with Germany. The project originated 
            in 2008 as a simplified version of the VLS-1 rocket, 
            using only the core stages.

            A version based on the S-50 rocket engine is being 
            developed, with the objective of launching satellites 
            of up to 150 kg into equatorial circular orbits at 
            300 km altitude.
            
            Development on VLM started in 2008 for the purpose of 
            low-cost and reliable launch of microsatellites. 
            Initially, a four-stage rocket using solid fuel was 
            proposed, arranged in the following order:

            Stage 1: S-43 rocket engine
            Stage 2: S-40TM rocket engine
            Stage 3: S-44 rocket engine
            Stage 4: S-33 rocket engine

            It was later decided in 2011 to build a precursor 
            single-stage rocket bearing a new engine called S-50. 
            The vehicle is being developed and its engine tested 
            in collaboration with the German Space Agency (DLR).
            This precursor test is called VS-50 and is planned for 
            launch in 2019. The VS-50 vehicle measures 12 m (39 ft) 
            long, 1.46 m (4 ft 9 in) in diameter, and has a mass of 
            about 15 tons.

            All launches are planned to take place from the Alcântara 
            Launch Center, located on Brazil's northern Atlantic coast.
            '''
    },
    "Feng Bao 1": {
        "Name": "Feng Bao 1",
        "Agency": "SAST - Shanghai Academy of Spaceflight Technology",
        "Payload Capacity to LEO": "2,500 kilograms (5,500 lb)",
        "Height": "33 metres (108 ft)",
        "Diameter": "3.35 metres (11.0 ft)",
        "Mass": "191,700 kilograms (422,600 lb)",
        "Years in Operation": "1972-1981",
        "Country": "China",
        "Operational Status": "Retired",
        "Number of Stages": "2",
        "Additional Information":
            '''
            The Feng Bao 1 (Chinese: 风暴; lit.: 'Storm'), also known 
            as FB-1, was a Chinese carrier rocket launched between 1972 
            and 1981. It was replaced by the nearly identical Long 
            March 2, which had been developed at the same time for 
            political reasons related to China's Cultural Revolution.

            The Feng Bao was derived from the DF-5 missile. Eleven 
            were launched, of which four failed. Launches occurred 
            from LA-2B at the Jiuquan Satellite Launch Centre.
            '''
    },
    "Kaituozhe-1": {
        "Name": "Kaituozhe-1",
        "Agency": "CASC - China Aerospace Science and Technology Corporation",
        "Payload Capacity to LEO": "100kg (220lbs)",
        "Height": "13.6m (44 ft)",
        "Diameter": "1.4m (4.5 ft)",
        "Mass": "18,143kg (4000 lbs)",
        "Years in Operation": "2002-2003",
        "Country": "China",
        "Operational Status": "Retired",
        "Number of Stages": "4",
        "Additional Information":
            '''
            Kaituozhe-1 (KT-1) was small, solid fueled launch vehicle 
            based on the road mobile DF-21 IRBM with an additional 
            upper stage (in total 4 stages[1]). It was 13.6 meters 
            in length and 1.4 meters in diameter, with launch mass 
            of 20t. It was possible to launch KT-1 both from a 
            truck-based platform or from airborne platform. It had 
            a 100 kg to LEO payload capacity. It was possibly the 
            launch vehicle for a Chinese ASAT system that was tested 
            against an old Chinese weather satellite in 2007.

            The vehicle has performed two flights, the first in 15 
            September 2002 and the second 16 September 2003. The 
            first flight failed to place a 50 kg satellite into 
            polar orbit due to a second stage malfunction. The 
            second flight was also a failure, however Chinese 
            officials declared some success citing the guidance 
            systems, fairing separation and satellite-launcher 
            separation as successful. The second launch sent the 
            payload, PS-2 microsatellite (40 kg) into wrong orbit. 
            The satellite completed barely one orbit before 
            re-entering the atmosphere.
            
            The Kaituozhe-1 launcher appears to have been cancelled 
            after two unsuccessful launches. A third (in 2004) and 
            fourth launch have been rumored, but are not confirmed.
                        
            The rocket had three variants: the Kaituozhe-1 (KT-1), 
            the Kaituozhe-1A (KT-1A, originally designated KT-2, not 
            to be confused with KT-2 below) and the Kaituozhe-1B 
            (KT-1B, originally designated KT-2A, not to be confused 
            with KT-2A below). The rockets that flew were of the KT-1 
            variant. The KT-1A and KT-1B variant rockets were not built.
            '''
    },

    "Kuaizhou": {
        "Name": "Kuaizhou",
        "Agency": "ExPace (Subsidiary of CASIC - China Aerospace Science and Industry Corporation)",
        "Payload Capacity to LEO": "",
        "Height": "19.4 m (64 ft)",
        "Diameter": "1.4 m (4 ft 7 in)",
        "Mass": "29,029 kg (64,000 lbs)",
        "Years in Operation": "2013~",
        "Country": "China",
        "Operational Status": "Active",
        "Number of Stages": "4",
        "Additional Information":
            '''
            Kuaizhou (KZ, Chinese: 快舟; pinyin: kuàizhōu, meaning 
            "speedy vessel") (also called Feitian Emergency Satellite 
            Launch System, Feitian-1, FT-1) is a family of Chinese 
            "quick-reaction" orbital launch vehicles. Flying since 
            2013, Kuaizhou 1 and 1A consist of three solid-fueled rocket 
            stages, with a liquid-fueled fourth stage as part of the 
            satellite system. Kuaizhou 11, which flew an unsuccessful 
            maiden flight in July 2020, is a larger model able to launch 
            a 1,500 kilograms (3,300 lb) payload into low Earth orbit. 
            Heavy-lift models KZ-21 and KZ-31 are in development. The 
            Kuaizhou series of rockets is manufactured by ExPace, a 
            subsidiary of China Aerospace Science and Industry Corporation 
            (CASIC), as their commercial launch vehicles.
            
            The rocket series is based on CASIC's ASAT and BMD mid-course 
            interceptor rockets, in particular the DF-21 IRBM (another 
            Chinese rocket that was based on DF-21 was the Kaituozhe-1). 
            Development on the KZ rockets started in 2009. The KZ rockets
            were to provide an integrated launch vehicle system with the 
            rapid ability to replace Chinese satellites that might be 
            damaged or destroyed in an act of aggression in orbit. The 
            vehicle uses mobile launch platform. The rocket is operated 
            by the Chinese 2nd Artillery.

            The maiden flight of Kuaizhou 1 rocket, orbiting the Kuaizhou 1 
            natural disaster monitoring satellite, occurred on 25 September 
            2013, launched from Jiuquan Satellite Launch Center.
            
            Second flight of Kuaizhou 1 rocket, orbiting the Kuaizhou 2 natural 
            disaster monitoring satellite, was launched at 06:37 UTC on 21 
            November 2014, again from Jiuquan Satellite Launch Center.
            
            The first commercial launch inaugurated the Kuaizhou 1A version 
            on 9 January 2017, from Jiuquan. It placed three small satellites 
            into a polar orbit.
            '''
    },
    "Long March 1": {
        "Name": "Long March 1",
        "Agency": '''
        MAI - Moscow Aviation Institute, 
        CASC - China Aerospace Science and Technology Corporation, 
        CAST - China Academy of Space Technology''',
        "Payload Capacity to LEO": "300 kilograms (660 lb)",
        "Height": "	29.86 metres (98.0 ft)",
        "Diameter": "2.25 metres (7.4 ft)",
        "Mass": "81,570 kilograms (179,830 lb)",
        "Years in Operation": "1970-1971",
        "Country": "China",
        "Operational Status": "Retired",
        "Number of Stages": "3",
        "Additional Information":
            '''
            The Long March 1 (长征一号), also known as the Changzheng-1 
            (CZ-1), was the first member of China's Long March rocket family.
            
            Development started in January 1965 as the Seventh Ministry 
            of Machinery Industry issued a design task. The two stage 
            liquid fueled DF-4 was modified by adding a third stage in 
            order to make it to the desired orbit. Long March 1's second 
            flight launched China's first satellite Dong Fang Hong 1 to 
            space on April 24, 1970. The rocket was operational during 
            1970–1971. Wang Xiji was the chief designer of the rocket.
            '''
    },
    "Long March 1D": {
        "Name": "Long March 1D",
        "Agency": '''
        MAI - Moscow Aviation Institute, 
        CASC - China Aerospace Science and Technology Corporation, 
        CAST - China Academy of Space Technology
        ''',
        "Payload Capacity to LEO": "",
        "Height": "28.22 m (92.6 ft)",
        "Diameter": "2.25 m (7.4 ft)",
        "Mass": "81,650 kg (180,010 lb)",
        "Years in Operation": "1995-2002",
        "Country": "China",
        "Operational Status": "Retired",
        "Number of Stages": "3",
        "Additional Information":
            '''
            Long March 1D was a member of China's Long March rocket 
            family. During the 1990s CALT developed an improved 
            version of the DF-4 to test the reentry vehicle warheads 
            of the DF-31.[6][7][8] They took advantage of this 
            development and offered it as the Long March 1D for 
            commercial application. The modifications included:

            An DF-4 improved first stage, which used the new version 
            of the YF-2B, and switched propellants to UDMH/N2O4 for 
            improved performance. The replacement of the DF-4 second 
            stage motor YF-3A. The proposed replacement was the Long 
            March 4 third stage engine, the YF-40. A new inline 
            inter-stage would replace the existing tapered connector 
            between the second and third stages, which allowed for an 
            additional 70cm diameter to be added to the third stage 
            skirt. This would allow for the addition of RCS to the 
            third stage. A new third stage with a new motor, the FG-36 
            and an optional RCS. A new computer inertial guidance system 
            which enabled the third stage to be 3-axis stabilised for 
            added precision. The new design did not have a good reception 
            and was only used for reentry vehicle tests. It flew three 
            suborbital missions from Taiyuan LC-1 with two successes and 
            a failure on the final mission. The first launch was on 
            June 1, 1995 and the second one was in November 1997. The 
            final and failed launch was on January 3, 2002.
            '''
    },
    "Falcon 9": {
        "Name": "Falcon 9",
        "Agency": "SpaceX",
        "Payload Capacity to LEO": "22,800 kg (50,300 lb)",
        "Height": "70 m (230 ft)",
        "Diameter": "3.7 m (12 ft)",
        "Mass": "549,054 kg (1,210,457 lbs)",
        "Years in Operation":
            '''
            FT Block 5: 2018~
            FT: 2015-2018
            v1.1: 2013-2016
            v1.0: 2010-2013
            ''',
        "Country": "USA",
        "Operational Status":
            '''
            FT Block 5: Active
            FT Block 4: Retired
            FT Block 3: Retired
            v1.1: Retired
            v1.0: Retired
            ''',
        "Number of Stages": "2",
        "Additional Information":
            '''
            Falcon 9 is a partially reusable two-stage-to-orbit 
            medium-lift launch vehicle designed and manufactured by 
            SpaceX in the United States. It is powered by Merlin 
            engines, also developed by SpaceX, burning cryogenic 
            liquid oxygen and rocket-grade kerosene (RP-1) as 
            propellants. Its name is derived from the fictional 
            Star Wars spacecraft, the Millennium Falcon, and the 
            nine Merlin engines of the rocket's first stage. The rocket 
            evolved with versions v1.0 (2010–2013), v1.1 (2013–2016), 
            v1.2 "Full Thrust" (2015–present), including the Block 5 
            Full Thrust variant, flying since May 2018. Unlike most 
            rockets, which are expendable launch systems, since the 
            introduction of the Full Thrust version, Falcon 9 is 
            partially reusable, with the first stage capable of 
            re-entering the atmosphere and landing vertically after 
            separating from the second stage. This feat was achieved 
            for the first time on flight 20 with the v1.2 version in 
            December 2015.
            
            Falcon 9 can lift payloads of up to 22,800 kilograms 
            (50,300 lb) to low Earth orbit, 8,300 kg (18,300 lb) to 
            geostationary transfer orbit (GTO) when expended, and 
            5,500 kg (12,100 lb) to GTO when the first stage is 
            recovered. The heaviest GTO payloads flown have been 
            Intelsat 35e with 6,761 kg (14,905 lb), and Telstar 19V 
            with 7,075 kg (15,598 lb). The latter was launched into a 
            lower-energy GTO orbit achieving an apogee well below the 
            geostationary altitude, while the former was launched into 
            an advantageous super-synchronous transfer orbit.
            
            In 2008, SpaceX won a Commercial Resupply Services (CRS) 
            contract in NASA's Commercial Orbital Transportation Services 
            (COTS) program to deliver cargo to the International Space 
            Station (ISS) using the Falcon 9 and Dragon capsule. The first 
            mission under this contract launched on October 8, 2012. Falcon 
            9 has been human-rated for transporting NASA astronauts to the 
            ISS as part of the NASA Commercial Crew Development program. 
            Currently, Falcon 9 has been certified for the National Security 
            Space Launch[22] program and NASA Launch Services Program as 
            "Category 3", which can launch the priciest, most important, and 
            most complex NASA missions.
            
            Five rockets of the version 1.0 design were launched from June 2010 
            to March 2013. Version 1.1 conducted fifteen launches from September 
            2013 to January 2016. The "Full Thrust" version was in service from 
            December 2015 into 2018, with several additional upgrades within 
            this version. The latest variant, Block 5, was introduced in May 
            2018. It features increased engine thrust, improved landing legs, and 
            other minor improvements to help recovery and reuse. The Falcon 
            Heavy derivative, introduced in February 2018, consists of a 
            strengthened Falcon 9 first stage as its center core, attached to 
            two standard Falcon 9 first stages used as boosters.
            '''
    },
    "Falcon Heavy": {
        "Name": "Falcon Heavy",
        "Agency": "SpaceX",
        "Payload Capacity to LEO": "3,800 kg (140,700 lb)",
        "Height": "70 m (230 ft)",
        "Diameter": "3.66 m (12.0 ft) (each booster)",
        "Mass": "12.2 m (40 ft)",
        "Years in Operation": "2018~",
        "Country": "USA",
        "Operational Status": "Active",
        "Number of Stages": "2+",
        "Additional Information":
            '''
            The Falcon Heavy is a partially reusable heavy-lift launch 
            vehicle designed and manufactured by SpaceX. It is derived 
            from the Falcon 9 vehicle and consists of a strengthened 
            Falcon 9 first stage as the center core with two additional 
            Falcon 9-like first stages as strap-on boosters. The Falcon 
            Heavy has the highest payload capacity of any currently 
            operational launch vehicle, the third-highest capacity of 
            any rocket ever to reach orbit, trailing the Saturn V and 
            Energia, and the third-highest capacity of any orbital-class 
            rocket ever launched successfully (behind the Saturn V and 
            Energia).

            SpaceX conducted the Falcon Heavy's maiden launch on February 6, 
            2018, at 3:45 p.m. EST (20:45 UTC). The rocket carried a Tesla
            Roadster belonging to SpaceX founder Elon Musk, carrying a dummy 
            dubbed "Starman", as a dummy payload. The second Falcon Heavy 
            launch occurred on April 11, 2019 and all three booster rockets 
            successfully returned to earth.[10] The third Falcon Heavy launch 
            successfully occurred on June 25, 2019. Since then, the Falcon 
            Heavy has been certified for the National Security Space Launch 
            program.

            The Falcon Heavy was designed to be able to carry humans into space 
            beyond low Earth orbit, although as of February 2018, SpaceX has 
            confirmed that they will not transport people on the Falcon Heavy, 
            nor pursue the human-rating certification process to transport NASA 
            astronauts. The Falcon Heavy and Falcon 9 will be replaced by the 
            Starship launch system.
            '''
    },

    "Atlas V": {
        "Name": "Atlas V",
        "Agency": "ULA - United Launch Alliance",
        "Payload Capacity to LEO": "",
        "Height": "58.3 m (191 ft)",
        "Diameter": "3.81 m (12.5 ft)",
        "Mass": "590,000 kg (1,300,000 lb)",
        "Years in Operation": "2002~",
        "Country": "USA",
        "Operational Status": "Active",
        "Number of Stages": "2",
        "Additional Information":
            '''
            Atlas V is the fifth major version in the Atlas rocket family. 
            It is an expendable launch system originally designed by 
            Lockheed Martin, now being operated by United Launch Alliance 
            (ULA), a joint venture between Lockheed and Boeing.

            Each Atlas V rocket consists of two main stages. The first 
            stage is powered by a Russian RD-180 engine manufactured by 
            RD Amross and burning kerosene and liquid oxygen. The Centaur 
            upper stage is powered by one or two US RL10 engine(s) 
            manufactured by Aerojet Rocketdyne and burning liquid 
            hydrogen and liquid oxygen. AJ-60A strap-on solid rocket 
            boosters (SRBs) are used in some configurations and will 
            be replaced by GEM-63 SRBs in the near future. The standard 
            payload fairings are 4 or 5 meters in diameter with various
            lengths.
            
            The Atlas V was developed by Lockheed Martin Commercial Launch 
            Services (LMCLS) as part of the US Air Force Evolved Expendable 
            Launch Vehicle (EELV) program and made its inaugural flight on 
            August 21, 2002. The vehicle operates from Space Launch Complex 
            41 at Cape Canaveral Air Force Station and Space Launch Complex 
            3-E at Vandenberg Air Force Base. LMCLS continued to market the 
            Atlas V to commercial customers worldwide until January 2018, 
            when ULA assumed control of commercial marketing and sales.
            '''
    },

}


# *** Class for Button Push ***

def pushDataToLabelTitle(data):
    return data["Name"]  # after fixing this, make sure to create a label placement and to delete data[name] below


def pushDataToLabel(data):
    return "\n" + "\n" + "Country: " + data["Country"] + "\n" + "Agency/Company: " + "\n" + data[
        "Agency"] + "\n" + "\n" + "Payload Capacity to LEO: " + data["Payload Capacity to LEO"] + "\n" + "Height: " \
           + data["Height"] + "\n" + "Diameter: " + data["Diameter"] + "\n" + "Mass: " + data["Mass"] + "\n" \
           + "Years in Operation: " + data["Years in Operation"] + "\n" + "\n" + "Additional Information: " + data[
               "Additional Information"]


# labelCreate = Label (mainWindowCenterFrame, text="poop", font="-weight bold")  **to create bold text**

# *** Button Functionality/Functions Definitions ***
def satVPushed():
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary['Saturn V']))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary["Saturn V"]))
    imgLabel.configure(image=satvphoto)


def soyuzPushed():
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary['Soyuz']))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary["Soyuz"]))
    imgLabel.configure(image=soyuzphoto)


def deltaIIIPushed():
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary['Delta III']))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary["Delta III"]))
    imgLabel.configure(image=deltaIIIphoto)


def ariane62Pushed():
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary['Ariane 62']))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary["Ariane 62"]))
    imgLabel.configure(image=ariane62photo)


def TronadorIIPushed():
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary['Tronador II']))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary["Tronador II"]))
    imgLabel.configure(image=tronadorIIphoto)


def vls1Pushed():
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary['VLS-1']))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary["VLS-1"]))
    imgLabel.configure(image=vls1photo)


def vlmPushed():
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary['VLM']))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary["VLM"]))
    imgLabel.configure(image=vlmphoto)


def fengbao1Pushed():
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary['Feng Bao 1']))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary["Feng Bao 1"]))
    imgLabel.configure(image=fengbao1photo)


def kaituozhe1Pushed():
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary['Kaituozhe-1']))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary["Kaituozhe-1"]))
    imgLabel.configure(image=kaituozhe1photo)


def kuaizhouPushed():
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary['Kuaizhou']))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary["Kuaizhou"]))
    imgLabel.configure(image=kuaizhouphoto)


def longMarch1Pushed():
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary['Long March 1']))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary["Long March 1"]))
    imgLabel.configure(image=longmarch1photo)


def longMarch1dPushed():
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary['Long March 1D']))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary["Long March 1D"]))
    imgLabel.configure(image=longmarch1Dphoto)

def falcon9Pushed():
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary['Falcon 9']))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary["Falcon 9"]))
    imgLabel.configure(image=falcon9photo)

def falconheavyPushed():
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary['Falcon Heavy']))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary["Falcon Heavy"]))
    imgLabel.configure(image=falconheavyphoto)

def atlasvPushed():
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary['Atlas V']))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary["Atlas V"]))
    imgLabel.configure(image=atlasVphoto)


def doNothing():
    print("Nothing happened, of course.")


def helpMenuVersionPushed():
    tkinter.messagebox.showinfo("Version", "0.1 Alpha")


# def helpAboutPopUp():
#   aboutPopUp = Toplevel(height=600, width=800)

def helpMenuAboutPushed():
    tkinter.messagebox.showinfo("About",
                                '''
    Developer: Seralyn Campbell

    Email: seralyncampbell@gmail.com

    Written in: Python 3.8.5

    Open Source Software: 
    https://github.com/Seralyn/rocket_info
                                ''')


def update_time():
    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    label['text'] = currentTime
    root.after(1, update_time)


def quit():
    root.quit()


# *** Popup Menus ***
'''
pop_up_answer = tkinter.messagebox.askquestion("Important Question:", "Do you want to learn more about rockets?")
if pop_up_answer == "yes":
    tkinter.messagebox.showinfo("Message", "I'm so happy to hear that!")
elif pop_up_answer == "no":
    tkinter.messagebox.showinfo("Message", "I see that you would love to learn more about rockets. That's wonderful.")
'''
# ***The Main Menu ***
menu = Menu(root)
root.config(menu=menu)

sortMenu = Menu(menu, bd=0, tearoff=FALSE)
menu.add_cascade(label="Sort", menu=sortMenu)
sortMenu.add_command(label="Alphabetical", command=doNothing)
sortMenu.add_command(label="Agency/Company", command=doNothing)
sortMenu.add_command(label="Country", command=doNothing)
sortMenu.add_command(label="Lifting Class", command=doNothing)
sortMenu.add_command(label="Operational Status", command=doNothing)
sortMenu.add_command(label="Payload Capacity to LEO", command=quit)
sortMenu.add_command(label="Mass", command=quit)
sortMenu.add_command(label="Diameter", command=quit)
sortMenu.add_command(label="Height", command=quit)

editMenu = Menu(menu, tearoff=FALSE)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=doNothing)
editMenu.add_command(label="Redo", command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Preferences...", command=doNothing)

helpMenu = Menu(menu, tearoff=FALSE)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=helpMenuAboutPushed)
helpMenu.add_command(label="Version", command=helpMenuVersionPushed)
helpMenu.add_command(label="List of Acronyms", command=doNothing)

# *** Create all Frames/Containers ***
toolbarFrame = Frame(root, bg="gray40", width=1200, height=20)
mainWindowFrame = Frame(root, bg="gray63", width=1200, height=650)
mainWindowLeftFrame = Frame(mainWindowFrame, bg="gray63", width=400, height=650, padx=10)
mainWindowCenterFrame = Frame(mainWindowFrame, bg="gray63", width=600, height=650)
mainWindowRightFrame = Frame(mainWindowFrame, bg="gray63", width=400, height=650)
statusBarFrame = Frame(root, bg="gray76", width=1350, height=20)

# layout parameters of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# *** Layout of all Frames/Containers ***
toolbarFrame.grid(row=0, sticky="ew")
mainWindowFrame.grid(row=1, sticky="nsew")
mainWindowLeftFrame.grid(row=0, column=0)
mainWindowCenterFrame.grid(row=0, column=1)
mainWindowCenterFrame.grid_propagate(FALSE)
mainWindowRightFrame.grid(row=0, column=2)

# *** Image definitions ***
satvphoto = PhotoImage(file="SaturnV.png")
soyuzphoto = PhotoImage(file="soyuz.png")
deltaIIIphoto = PhotoImage(file="delta iii.png")
ariane62photo = PhotoImage(file="ariane 62.png")
tronadorIIphoto = PhotoImage(file="tronador ii.png")
vls1photo = PhotoImage(file="vls1.png")
vlmphoto = PhotoImage(file="vlm.png")
fengbao1photo = PhotoImage(file="fengbao1.png")
kaituozhe1photo = PhotoImage(file="kaituozhe1.png")
kuaizhouphoto = PhotoImage(file="kuaizhou.png")
longmarch1photo = PhotoImage(file="longmarch1.png")
longmarch1Dphoto = PhotoImage(file="longmarch1d.png")
falcon9photo = PhotoImage(file="falcon9.png")
falconheavyphoto = PhotoImage(file="falconheavy.png")
atlasVphoto = PhotoImage(file="atlasv.png")

# *** Create all buttons/Labels ***
insertButton = Button(toolbarFrame, text="Insert Image", command=doNothing)
printButton = Button(toolbarFrame, text="Print", command=doNothing)

rocketListLabel = Label(mainWindowLeftFrame, bg="gray63", text="Rockets:", font="-weight bold")

satVButton = Button(mainWindowLeftFrame, pady=4, relief=FLAT, bg="gray63", fg="white", text="Saturn V", bd=0,
                    command=satVPushed)
soyuzButton = Button(mainWindowLeftFrame, pady=4, text="Soyuz", bg="gray63", fg="white", bd=0, command=soyuzPushed)
deltaIIIButton = Button(mainWindowLeftFrame, pady=4, text="Delta III", bg="gray63", fg="white", bd=0,
                        command=deltaIIIPushed)
ariane62Button = Button(mainWindowLeftFrame, pady=4, text="Ariane 62", bg="gray63", fg="white", bd=0,
                        command=ariane62Pushed)
TronadorIIButton = Button(mainWindowLeftFrame, pady=4, text="Tronador II", bg="gray63", fg="white", bd=0,
                          command=TronadorIIPushed)
vls1Button = Button(mainWindowLeftFrame, pady=4, text="VLS-1", bd=0, bg="gray63", fg="white", command=vls1Pushed)
vlmButton = Button(mainWindowLeftFrame, pady=4, text="VLM", bg="gray63", fg="white", bd=0, command=vlmPushed)
fengBao1Button = Button(mainWindowLeftFrame, pady=4, text="Feng Bao 1", bg="gray63", fg="white", bd=0,
                        command=fengbao1Pushed)
kaituozhe1Button = Button(mainWindowLeftFrame, pady=4, text="Kaituozhe-1", bg="gray63", fg="white", bd=0,
                          command=kaituozhe1Pushed)
kuaizhouButton = Button(mainWindowLeftFrame, pady=4, text="Kuaizhou", bg="gray63", fg="white", bd=0,
                        command=kuaizhouPushed)
longMarch1Button = Button(mainWindowLeftFrame, pady=4, text="Long March 1", bg="gray63", fg="white", bd=0,
                          command=longMarch1Pushed)
longMarch1DButton = Button(mainWindowLeftFrame, pady=4, text="Long March 1D", bg="gray63", fg="white", bd=0, command=longMarch1dPushed)
falcon9Button = Button(mainWindowLeftFrame, pady=4, text="Falcon 9", bg="gray63", fg="white", bd=0, command=falcon9Pushed)
falconHeavyButton = Button(mainWindowLeftFrame, pady=4, text="Falcon Heavy", bg="gray63", fg="white", bd=0, command=falconheavyPushed)
atlasVButton = Button(mainWindowLeftFrame, pady=4, text="Atlas V", bg="gray63", fg="white", bd=0, command=atlasvPushed)
slsButton = Button(mainWindowLeftFrame, pady=4, text="S.L.S. (Space Launch System)", bg="gray63", fg="white", bd=0)
newGlennButton = Button(mainWindowLeftFrame, pady=4, text="New Glenn", bg="gray63", fg="white", bd=0)
hIIAButton = Button(mainWindowLeftFrame, pady=4, text="HII-A", bg="gray63", fg="white", bd=0)
diamantButton = Button(mainWindowLeftFrame, pady=4, text="Diamant", bg="gray63", fg="white", bd=0)
otragButton = Button(mainWindowLeftFrame, pady=4, text="OTRAG", bg="gray63", fg="white", bd=0)
lambdaButton = Button(mainWindowLeftFrame, pady=4, text="Lambda", bg="gray63", fg="white", bd=0)
l4sButton = Button(mainWindowLeftFrame, pady=4, text="L-4S", bg="gray63", fg="white", bd=0)
muButton = Button(mainWindowLeftFrame, pady=4, text="Mu", bg="gray63", fg="white", bd=0)
m4sButton = Button(mainWindowLeftFrame, pady=4, text="M-4S", bg="gray63", fg="white", bd=0)

rocketName = Label(mainWindowCenterFrame, font="-weight bold", bg="gray63", fg="white")
rocketName.config(font=("Arial", 20))
infoLabel = Label(mainWindowCenterFrame, bg="gray63", fg="white")
infoLabel.config(font=("Arial", 11))

imgLabel = Label(mainWindowRightFrame, bg="gray63", border=0, padx=20)  # padx does nothing...why?

label = Label(statusBarFrame, text="placeholder")
label.grid(row=0, column=0)

# *** Placement & Layout of all Buttons ***
insertButton.grid(row=0, column=0, padx=3, pady=4, sticky=W)
printButton.grid(row=0, column=1, padx=3, pady=4, sticky=W)

rocketListLabel.grid(row=0, column=0, padx=60, pady=5, sticky=N)

satVButton.grid(row=1, column=0, padx=15)
soyuzButton.grid(row=2, column=0, padx=15)
deltaIIIButton.grid(row=3, column=0, padx=15)
ariane62Button.grid(row=4, column=0, padx=15)
TronadorIIButton.grid(row=5, column=0, padx=15)
vls1Button.grid(row=8, column=0, padx=15)
vlmButton.grid(row=9, column=0, padx=15)
fengBao1Button.grid(row=10, column=0, padx=15)
kaituozhe1Button.grid(row=11, column=0, padx=15)
kuaizhouButton.grid(row=12, column=0, padx=15)
longMarch1Button.grid(row=13, column=0, padx=15)
longMarch1DButton.grid(row=14, column=0, padx=15)
falcon9Button.grid(row=15, column=0, padx=15)
falconHeavyButton.grid(row=16, column=0, padx=15)
atlasVButton.grid(row=17, column=0, padx=15)
slsButton.grid(row=18, column=0, padx=15)
newGlennButton.grid(row=19, column=0, padx=15)
hIIAButton.grid(row=20, column=0, padx=15)
diamantButton.grid(row=21, column=0, padx=15)
otragButton.grid(row=22, column=0, padx=15)
lambdaButton.grid(row=23, column=0, padx=15)
l4sButton.grid(row=24, column=0, padx=15)
muButton.grid(row=25, column=0, padx=15)
m4sButton.grid(row=26, column=0, padx=15)

rocketName.grid(row=0, column=0)
infoLabel.grid(row=1, column=0, padx=25)

imgLabel.grid(row=0, column=0, sticky=E)

statusBarFrame.grid(row=2)
statusBarFrame.grid_propagate(FALSE)

# sticky EW seems to do nothing here. How can I stretch the status bar out to the size of the whole frame?

# *** Add Image ***
# satvphoto = PhotoImage(file="SaturnV.png")
# satvlabel = Label(root, image=satvphoto)
# satvlabel.grid(anchor=E)   #find out why this can't anchor to the right of the sorting options


'''If you want to handle jpg as well as png, import Image and ImageTk from PIL then do:
image = Image.open("Image Name")
photo = ImageTk.PhotoImage(image)'''

update_time()
root.mainloop()
