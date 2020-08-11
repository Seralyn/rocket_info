from tkinter import *

root = Tk()
frame = Frame()
root.geometry("600x600")

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
    }
}


def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    entry_text = w.get(index)
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary[entry_text]))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary[entry_text]))
    print(entry_text)

def pushDataToLabelTitle(data):
    return data["Name"]


def pushDataToLabel(data):
    return "\n" + "\n" + "Country: " + data["Country"] + "\n" + "Agency/Company: " + "\n" + data[
        "Agency"] + "\n" + "\n" + "Payload Capacity to LEO: " + data["Payload Capacity to LEO"] + "\n" + "Height: " \
           + data["Height"] + "\n" + "Diameter: " + data["Diameter"] + "\n" + "Mass: " + data["Mass"] + "\n" \
           + "Years in Operation: " + data["Years in Operation"] + "\n" + "\n" + "Additional Information: " + data[
               "Additional Information"]

lb = Listbox(frame, name='lb')
rocket_info_frame = Frame(root, width=500, height=700)
rocket_info_frame.grid_propagate(FALSE)
rocket_info_frame.grid(row=0, column=1)
rocketName = Label(rocket_info_frame, text="")
rocketName.grid(row=0, column=0)
infoLabel = Label(rocket_info_frame, text="")
infoLabel.grid(row=1, column=0)


lb.bind('<<ListboxSelect>>', onselect)

frame.grid(row=0, column=0)
lb.grid(row=0, column=0)


lb.insert(0, "Saturn V")
lb.insert(1, "Soyuz")
lb.insert(2, "Delta III")
lb.insert(3, "Ariane 62")
lb.insert(4, "Tronador II")

root.mainloop()