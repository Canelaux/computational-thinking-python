# PSET 1
def greedy_cow_transport(cow_dict, weight_limit):
    dict_cow = cow_dict.copy()
    list_trips = []

    while dict_cow:
        trip = []
        remaining_weight = weight_limit

        sorted_cows = sorted(dict_cow, key=dict_cow.get, reverse=True)

        for cow in sorted_cows:
            if dict_cow[cow] <= remaining_weight:
                trip.append(cow)
                remaining_weight -= dict_cow[cow]

        for cow in trip:
            dict_cow.pop(cow)

        list_trips.append(trip)

    return list_trips

def brute_force_cow_transport(cow_dict, weight_limit):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    dict_cow = cow_dict.copy()
    list_trips = []
    for lista in (sorted(get_partitions(list(dict_cow.keys())), key =len)):
    # print('esta es la lista de get_partitions',lista)
        list_trips = []
        for cows in lista:
            # print('Estas son las vacas en el viaje', cows)
            trip = []
            remaining_weight = weight_limit
            for cow in cows:
                if dict_cow[cow] <= remaining_weight:
                    trip.append(cow)
                    remaining_weight -= dict_cow[cow]

                else:
                    # rompase porque no sirvio la combinacion
                    break
            list_trips.append(trip)
        if lista == list_trips:
            return list_trips
        
# PSET 2
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width: int, height:int):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.clean_tiles = []
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # Remember pos is an instance of an Position class
        # So that we can access its attributes and store them
        # in a tuple
        
        position = (int(pos.getX()), int(pos.getY()))
        if position not in self.clean_tiles:
            self.clean_tiles.append(position)

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # En primera implementación que pensé, no se asignan los valores de m y n 
        # como atributos del objeto. En cambio, se utilizan directamente 
        # en el bucle for y la comparación dentro de la función isTileCleaned. 
        # Esto implica que m y n solo estarán disponibles dentro del ámbito 
        # de la función isTileCleaned y no podrán ser utilizados en otras partes del objeto.
        # tup = (m,n)
        
        # lo mejor es usar:
        self.m = m
        self.n = n
        # Esto implica que self.m y self.n estarán disponibles para otros métodos
        # de la misma clase y pueden ser utilizados en diferentes partes del objeto.
        
        tup = (self.m, self.n)
        for position in self.clean_tiles:
            if tup == position:
                return True
        else:
            return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        total_tiles = self.width * self.height
        return total_tiles

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        total_cleaned_tiles = len(self.clean_tiles)
        return total_cleaned_tiles

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        ram_pos = (
            Position(
                random.uniform(0, self.width),
                random.uniform(0, self.height))
        )
        return ram_pos

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if pos.getX() >= 0 and int(pos.getX()) < self.width and pos.getY() >= 0 and int(pos.getY())< self.height:
            return True
        else:
            return False
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # room is a RectangularRoom instance so it has its methods
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        # Think of direction as an angle
        self.direction = random.randint(0, 359)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """     
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        robot_position = self.getRobotPosition()
        new_position = robot_position.getNewPosition(self.getRobotDirection(), self.speed)
        if self.room.isPositionInRoom(new_position):
            self.setRobotPosition(new_position)
            self.room.cleanTileAtPosition(new_position)
        else:
            self.setRobotDirection(random.randint(0, 359))
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    # I need to store where
    fraction_cleaned_trials = []

    for trial in range(0, num_trials):
        count = 0
        # I need a room: I have widht and height
        room = RectangularRoom(width,height)
        # I need a robot or NUM_ROBOTS robots: I have speed, num_robot, and room
        # I need a list of robots. I have to take into account the robot_type
        # instanciating many robots of type robot_type as num_robots parameter
        # En una habitacion pueden haber mas de un robot al tiempo
        robots_list = [robot_type(room, speed) for robot in range(0, num_robots)]
        # La fraccion limpia de la habitacion se verifica con el ratio entre 
        # el numero de baldosas limpias / el numero de baldosas en total
        while room.getNumCleanedTiles()/room.getNumTiles() < min_coverage:
            # Cambiamos el contador el numero de PASOS REQUERIDOS PARA LIMPIAR UNA SOLA SIMULACION
            count += 1
            # Cada robot pasa y limpia una sola vez
            for robot in robots_list:
                robot.updatePositionAndClean()
                # Cambiamos el contador el numero de veces que lleva limpiando CADA ROBOT EN TODAS LAS SIMULACIONES
                # count += 1
            # Si en esa vez ya limpio la fraccion solicitada se detiene
            if room.getNumCleanedTiles()/room.getNumTiles() >=  min_coverage:
                # tiene que almacenar cuantas pasadas dio en fraction_cleaded_trials
                fraction_cleaned_trials.append(count)
            else:
                continue
    return sum(fraction_cleaned_trials)/num_trials

class RandomWalkRobot(Robot):

    def updatePositionAndClean(self):

        next_position = self.getRobotPosition().getNewPosition(random.randint(0, 359), self.speed)
        if self.room.isPositionInRoom(next_position) == False:
            self.setRobotDirection(random.randint(0, 359))
        else:
            self.setRobotPosition(next_position)
            self.setRobotDirection(random.randint(0, 359))
            self.room.cleanTileAtPosition(next_position)

#PSET 3
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        # clear_prob representa la probabilidad de que la partícula de virus sea eliminada del cuerpo del paciente en un paso de tiempo.
        # Mi interpretacion estaba mal porque deberia decir algo como: 
        # devuelve True (es decir se elimina) si el valor esta debajo de la probalilidad de que la particula de virus sea elminada del cuerpo del paciente en un paso de tiempo
        
        # choices = [True, False]
        # clearead_decision = random.choice(choices)
        # if cleared_decision:
        #     return True
        # else:
        #     return False
        
        return random.random() < self.clearProb

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        
        self.popDensity = popDensity #virus population / maximum populaation
        
        # como sabemos si se reproduce: The virus particle reproduces with probability
        # sellf.maxBirthProb * (1 - popDensity)
        if random.random() < self.maxBirthProb * (1 - self.popDensity):
            return SimpleVirus(self.getMaxBirthProb() , self.getClearProb())
       
        else:
            raise NoChildException()



class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """

        return len(self.viruses)       


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        viruses_list = self.viruses[:] 
        self.viruses = list(filter(lambda virus: not virus.doesClear(), viruses_list))
        popDensity = len(self.viruses) / self.maxPop
        
        viruses_list_2 = self.viruses
        for virus in viruses_list_2:
            try:
                offspring = virus.reproduce(popDensity)
                self.viruses.append(offspring)
            except NoChildException:
                continue
        return self.getTotalPop()
    
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """   
    for trial in range(0, numTrials):
        viruses_list = [SimpleVirus(maxBirthProb, clearProb) for virus in range(numViruses)]
        #sabemos que al patient se le pasa viruses_list y maxPop
        #cuántos pacientes se crean?
        simul_patient = Patient(viruses_list, maxPop)
        #This return a list of ints with the new total for each iteration
        average_pop = [simul_patient.update()/numTrials for step in range(300)]
    pylab.plot(average_pop, [i for i in range(300)])
    pylab.xlabel('Average Virus Population')
    pylab.ylabel('Time Step')
    pylab.title('Changes in virus pop for 300 time steps')
    pylab.legend(loc = 'upper left',title="Legend title", fontsize='small', fancybox=True)
    pylab.show()

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """

        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        
        #What happen if the drug is not in the resistances dict?
        
        return self.resistances.get(drug, False)


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        self.popDensity = popDensity
        self.activeDrugs = activeDrugs
        
        # Si es resistente a todas las drogas se reproduce con prob self.maxBirthProb * (1 - popDensity).
        if all(self.isResistantTo(drug) for drug in self.activeDrugs):
            if random.random() < self.maxBirthProb * (1 - self.popDensity):
                for drug in self.resistances:
                    inheritance_outcome = random.random()
                    if inheritance_outcome < self.mutProb:
                        if self.resistances[drug] == True:
                            self.resistances[drug] = False
                        else:
                            self.resistances[drug] = True
                return ResistantVirus(self.maxBirthProb, self.clearProb, self.resistances, self.mutProb)    
                # if random.random() < self.mutProb:
                #     #la que es True cambia a false
                #     for key in self.resistances.keys():
                #         self.resistances[key] = False
                #     return ResistantVirus(super().maxBirthProb, super().clearProb, resistances, super().mutProb)    
                # # else: the child resistances stays the same as the parent class
                # else:
                #     ResistantVirus(super().maxBirthProb, super().clearProb, resistances, super().mutProb)
            else:
                raise NoChildException()
        else:
            raise NoChildException()
        
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """

        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        
        #What happen if the drug is not in the resistances dict?
        
        return self.resistances.get(drug, False)


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        self.popDensity = popDensity
        self.activeDrugs = activeDrugs
        
        # Si es resistente a todas las drogas se reproduce con prob self.maxBirthProb * (1 - popDensity).
        if all(self.isResistantTo(drug) for drug in self.activeDrugs):
            if random.random() < self.maxBirthProb * (1 - self.popDensity):
                # si mutProb is succesfull the child resistance switches
                # For each drug check if change its status to False or True
                for drug in self.resistances:
                    if random.random() < self.mutProb:
                        if self.resistances[drug] == True:
                            self.resistances[drug] = False
                        else:
                            self.resistances[drug] = True
                return ResistantVirus(self.maxBirthProb, self.clearProb, self.resistances, self.mutProb)    
            else:
                raise NoChildException()
        else:
            raise NoChildException()

            

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """

        Patient.__init__(self, viruses, maxPop)
        self.drugs_administered = []

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """

        self.newDrug = newDrug
        if self.newDrug not in self.drugs_administered:
            self.drugs_administered.append(self.newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        # parece que es self.postcondition
        return self.drugs_administered

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        # Para cada virus en self.viruses revise si es resistente a todas las drogas en drugResist
        # Retorna el total de virus que es resistente a todas las drogas de la lista
        # count = 0
        # for virus in self.viruses:
        #     if all(virus.isResistanTo(drug) for drug in drugResis):
        #         count += 1
        # return count 
        resist_list = [all(virus.isResistantTo(drug) for drug in drugResist) for virus in self.viruses]
        count = sum(resist_list)
        return count


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """

        viruses_list = self.viruses[:]
        self.viruses = [virus for virus in viruses_list if not virus.doesClear()]
        popDensity = len(self.viruses) / self.maxPop
        
        viruses_iter = self.viruses[:]
        for virus in viruses_iter:
            try:
                # drugs being administered should be accounted for in the determination of whether each virus particle reproduces.
                # That means use getPrescriptions()
                offspring = virus.reproduce(popDensity,self.getPrescriptions())
                self.viruses.append(offspring)
            except NoChildException:
                continue
        return self.getTotalPop()
    
#PSET 4
# Problem 1
def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).
    Args:
        x: a list with length N, representing the x-coords of N sample points
        y: a list with length N, representing the y-coords of N sample points
        degs: a list of degrees of the fitting polynomial
    Returns:
        a list of numpy arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    list_of_models = []
    for deg in degs:
        xVals = np.array(x)
        yVals = np.array(y)
        model = np.polyfit(xVals, yVals, deg)
        list_of_models.append(model)
    return list_of_models

# Problem 2
def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    y = np.array(y)
    estimated = np.array(estimated)
    mean = np.mean(y)
    numerator = np.sum((y-estimated)**2)
    denominator = np.sum((y-mean)**2)
    r_squared = 1- (numerator/denominator)
    return r_squared

# Problem 3
import matplotlib.pyplot as plt
def evaluate_models_on_training(x, y, models):
    for model in models:
        estY = np.polyval(model, x)
        rSq = r_squared(y, estY)
        plt.figure()
        plt.plot(x, y, "bo")
        plt.plot(x, estY, "r")
        plt.xlabel("Years")
        plt.ylabel("temperature Highs, Celsius")
        plt.title("Evaluation of model" + "\n"
                    + str(model) + "\n" + "RSq = " + str(rSq))
        plt.show()


### Begining of program
raw_data = Climate('data.csv')

# Problem 3
y = []
x = INTERVAL_1
for year in INTERVAL_1:
    y.append(raw_data.get_daily_temp('BOSTON', 1, 10, year))
models = generate_models(x, y, [1])
evaluate_models_on_training(x, y, models)

# Problem 4: FILL IN MISSING CODE TO GENERATE y VALUES
x1 = INTERVAL_1
x2 = INTERVAL_2
y = []
for year in INTERVAL_1:
    y.append(np.mean(raw_data.get_yearly_temp('BOSTON', year)))
models = generate_models(x, y, [1])    
evaluate_models_on_training(x, y, models)