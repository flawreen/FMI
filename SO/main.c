#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
#include <string.h>
#include <time.h>


// Structura pentru a stoca datele despre programare
typedef struct {
    sem_t semaphore;
    char *clientName;
    int serviceTime;
} ServiceAppointment;

// Initializare programare
void appointmentOpen(ServiceAppointment *appointment, const char *clientName, int serviceTime) {
    sem_init(&appointment->semaphore, 0, 1);
    appointment->clientName = (char *)malloc(strlen(clientName) + 1);
    strcpy(appointment->clientName, clientName);
    appointment->serviceTime = serviceTime;
}

// Eliberare resurse programare
void appointmentClose(ServiceAppointment *appointment) {
    sem_destroy(&appointment->semaphore);
    free(appointment->clientName);
}

// Asteapta programare
void appointmentWait(ServiceAppointment *appointment) {
    sem_wait(&appointment->semaphore);
}

// Semnalizeaza programare
void appointmentSignal(ServiceAppointment *appointment) {
    sem_post(&appointment->semaphore);
}

// Functie pentru thread-uri care asteapta programare
void *serviceThreadFunction(void *arg) {
    ServiceAppointment *appointment = (ServiceAppointment *)arg;

    printf("%s asteapta %d secunde...\n", appointment->clientName, appointment->serviceTime);
    sleep(appointment->serviceTime); // Simulare timp de service
    printf("%s a terminat programarea.\n", appointment->clientName);

    // Semnalizeaza clientul ca service-ul a fost terminat
    appointmentSignal(appointment);

    return NULL;
}

void startActivitate(int nr_masini) {
    ServiceAppointment appointments[nr_masini];
    pthread_t threads[nr_masini];

    char nume[26][50];
    for(int j = 0; j < 26; ++j) {
        strcpy(nume[j], "Masina ");
        nume[j][7] = 'a' + j;
        nume[j][8] = '\0';
    }

    // cream threadurile
    for (int i = 0; i < nr_masini; ++i) {
        appointmentOpen(&appointments[i], nume[i], i + 2);  // (rand() % 8 + 1)
        if (pthread_create(&threads[i], NULL, serviceThreadFunction,  (void *)&appointments[i]) != 0) {
            perror("Eroare la crearea thread-ului");
            exit(EXIT_FAILURE);
        }
    }

    for (int i = 0; i < nr_masini; ++i) {
        appointmentWait(&appointments[i]);
        if (pthread_join(threads[i], NULL) != 0) {
            perror("Eroare la asteptarea thread-ului");
            exit(EXIT_FAILURE);
        }
        appointmentClose(&appointments[i]);
    }


}

void initializareActivitate(char* nume_fisier) {
    FILE *fisier;
    int nr_masini;

    fisier = fopen(nume_fisier, "r");

    if (fisier == NULL) {
        perror("Configuratia service-ului primita nu poate fi citita.");
        return;
    }

    if (fscanf(fisier, "%d", &nr_masini) == 1) {
        printf("A fost initializat service-ul in care vor intra %d masini.\n", nr_masini);
    } else {
        perror("eroare la citirea din fisier");
    }
    fclose(fisier);
    startActivitate(nr_masini);
}

int start() {
    printf("Meniu:\n");
    printf("1) Simuleaza activitatea de service 1\n");
    printf("2) Simuleaza activitatea de service 2\n");
    printf("3) Simuleaza activitatea de service 3\n");
    printf("4) Simuleaza activitatea de service 4\n");
    printf("0) Iesi din program\n");
    printf("Introduceti cifra activitatii: ");
    int optiune;
    fflush(0);
    scanf("%d", &optiune);
    clock_t start, end;

    switch(optiune) {
        case 1:
//            start = clock();
            initializareActivitate("service1.in");
//            end = clock();
//            double timp1 = ((double)(end - start)) / CLOCKS_PER_SEC;
//            printf("\n\nTimp set: %.6f\n\n", timp1);
            break;
        case 2:
//            start = clock();
            initializareActivitate("service2.in");
//            end = clock();
//            double timp2 = ((double)(end - start)) / CLOCKS_PER_SEC;
//            printf("\n\nTimp set: %.6f\n\n", timp2);
            break;
        case 3:
//            start = clock();
            initializareActivitate("service3.in");
//            end = clock();
//            double timp3 = ((double)(end - start)) / CLOCKS_PER_SEC;
//            printf("\n\nTimp set: %.6f\n\n", timp3);
            break;
        case 4:
//            start = clock();
            initializareActivitate("service4.in");
//            end = clock();
//            double timp4 = ((double)(end - start)) / CLOCKS_PER_SEC;
//            printf("\n\nTimp set: %.6f\n\n", timp4);
            break;
        default:
            return 0;
    }
    return 1;
}

int main() {

    while(start() == 1) {
        fflush(0);
        start();
        fflush(0);
    }


    return 0;
}
