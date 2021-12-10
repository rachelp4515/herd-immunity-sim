
class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       repro_rate, initial_infected):
      
        f = open(self.file_name, 'w')
        f.write(f' ~-~-~HERD IMMUNITY SIMULATION~-~-~\n')
        f.write('\n')
        f.write(f'Population Size: {pop_size}\n Initially Vaccinated: {vacc_percentage * 100}%\n Initially Infected: {initial_infected}\n Virus: {virus_name}\n Mortality Rate: {mortality_rate}\n Reproductive Rate: {repro_rate}\n ')
        f.write(f'~ beginning simulation...\n')
        f.close()


    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        f = open(self.file_name, 'a')
        if random_person_sick:
            f.write(f'Person {person._id} did not infect person {random_person._id} because they are already infected.\n')
        elif random_person_vacc:
            f.write(f'Person {person._id} did not infect person {random_person._id} because they are vaccinated.\n')
        else: 
            f.write(f'Person {person._id} infects person {random_person._id} \n')
        f.close()


    def log_infection_survival(self, person, survived_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        f = open(self.file_name, 'a')

        if survived_infection:
            f.write(f'Person #{person._id} survived. \n')
        else:
            f.write(f'Person #{person._id} died. \n')
        f.close()

    def log_time_step(self, time_step_number, newly_infected, newly_dead, total_living, total_vaccinated, total_dead):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        f = open(self.file_name, 'a')
        f.write(f'~~Step {time_step_number}~~\n Newly infected: {newly_infected}\n New deaths: {newly_dead}\n Amount alive: {total_living}\n Amount vaccinated: {total_vaccinated}\n Amount dead: {total_dead}\nTime step {time_step_number} ended, beginning {time_step_number + 1}\n')
       
        f.write(f'~~~\n')
        f.close()


    def log_summary(self, total_living, total_dead, total_vaccinated, number_interactions, vaccine_interactions, death_interactions):
        f = open(self.file_name, 'a')
        f.write('\n')
        f.write(f'~ Summary of Simulation ~ \n')
        f.write(f'Amount living: {total_living}\n')
        f.write(f'Amount dead: {total_dead}\n')
        f.write(f'Amount of vaccinations: {total_vaccinated}\n')
        f.write(f'Total number of interactions: {number_interactions}\n')
        f.write(f'Number vaxxed after interacting: {vaccine_interactions}\n')
        f.write(f'Number dead after interacting: {death_interactions}\n')
        f.close()
        




