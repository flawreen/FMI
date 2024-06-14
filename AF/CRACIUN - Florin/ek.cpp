//
//#include <iostream>
//#include <fstream>
//#include <vector>
//#include <queue>
//
//const int NMAX = 1001;
//const int INF = 1e9;
//
//std::ifstream fin("C:\\Users\\craci\\CLionProjects\\leetcode\\retea.in");
//
//int N, M, Start, End;
//int Capacitate[NMAX][NMAX];
//int Flux[NMAX][NMAX];
//int Flux_Invers[NMAX][NMAX];
//int InNod[NMAX], OutNod[NMAX];
//int Viz[NMAX], Tata[NMAX];
//bool eOk = true;
//void Citire()
//{
//    fin >> N >> Start >> End >> M;
//    for (int i = 1; i <= M; ++i)
//    {
//        int x, y, capacitate, flux;
//        fin >> x >> y >> capacitate >> flux;
//        Capacitate[x][y] = capacitate;
//        Flux[x][y] = flux;
//        Flux_Invers[y][x] = -flux;
//
//        if (flux > capacitate)
//            eOk = false;
//        InNod[y] += flux;
//        OutNod[x] += flux;
//    }
//    for (int i = 1; i <= N; ++i)
//    {
//        if (i != Start && i != End)
//        {
//            if (InNod[i] != OutNod[i])
//                eOk = false;
//        }
//    }
//    if (OutNod[Start] != InNod[End])
//        eOk = false;
//}
//
//int Bfs()
//{
//    std::queue<int>Q;
//    Q.push(Start);
//    Viz[Start] = 1;
//    while (!Q.empty())
//    {
//        int nod = Q.front();
//        Q.pop();
//        for (int i = 1; i <= N; ++i)
//        {
//            if (!Viz[i] && i != nod && (Capacitate[nod][i] - Flux[nod][i] > 0 || Flux_Invers[nod][i]<0))
//            {
//                Viz[i] = 1;
//                Q.push(i);
//                Tata[i] = nod;
//                if (i == End)
//                    return 1;
//            }
//        }
//    }
//    return 0;
//}
//
//void Fork_Fulkerson()
//{
//    while (Bfs())
//    {
//
//        int nod = End;
//        int min = INF;
//        while (Tata[nod])
//        {
//            std::cout << nod << " ";
//            int t = Tata[nod];
//            if (Capacitate[t][nod] - Flux[t][nod] > 0)
//                min = std::min(min, Capacitate[t][nod] - Flux[t][nod]);
//            else min = std::min(min, -Flux_Invers[t][nod]);
//            nod = t;
//        }
//        nod = End;
//        while (nod)
//        {
//            if (Capacitate[Tata[nod]][nod] - Flux[Tata[nod]][nod] > 0)
//            {
//                Flux[Tata[nod]][nod] += min;
//                Flux_Invers[nod][Tata[nod]] -= min;
//            }
//            else
//            {
//                Flux[nod][Tata[nod]] -= min;
//                Flux_Invers[Tata[nod]][nod] += min;
//            }
//            nod = Tata[nod];
//        }
//
//        std::cout << '\n';
//        for (int i = 1; i <= N; ++i)
//        {
//            Viz[i] = 0;
//            Tata[i] = 0;
//        }
//    }
//}
//
//void Bfs_Afis()
//{
//    std::queue<int>Q;
//    Q.push(Start);
//    while (!Q.empty())
//    {
//        int nod = Q.front();
//        Q.pop();
//        for (int i = 1; i <= N; ++i)
//        {
//            if (Capacitate[nod][i])
//            {
//                std::cout << nod << " " << i << " " << Flux[nod][i] << '\n';
//                if (!Viz[i])
//                {
//                    Q.push(i);
//                    Viz[i] = 1;
//                }
//            }
//        }
//    }
//}
//
//void Taietura()
//{
//    std::queue<int>Q;
//    Q.push(Start);
//    while (!Q.empty())
//    {
//        int nod = Q.front();
//        Q.pop();
//        for (int i = 1; i <= N; ++i)
//        {
//            if (Capacitate[nod][i])
//            {
//                if (Capacitate[nod][i] == Flux[nod][i])
//                    std::cout << nod << " " << i << '\n';
//                else
//                    Q.push(i);
//            }
//        }
//    }
//}
//
//void Afisare()
//{
//    std::cout << "DA\n";
//    int flux = 0;
//    for (int i = 1; i <= N; ++i)
//        std::cout << Flux[Start][i] << " ";
//    std::cout << flux << '\n';
////    for (int i = 1; i <= N; ++i)
////        Viz[i] = 0;
////    Bfs_Afis();
////    std::cout << flux << '\n';
////    Taietura();
//}
//
//int main()
//{
//    Citire();
//    if (!eOk)
//        std::cout << "NU\n";
//    else
//    {
//        Fork_Fulkerson();
//        Afisare();
//    }
//}
