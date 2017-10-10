// https://open.kattis.com/problems/cd
#include <iostream>
#include <vector>
void CD()
{
    long jackCount;
    std::cin >> jackCount;
    long jillCount;
    std::cin >> jillCount;
    std::vector<long> jackVector;
    std::vector<long> jillVector;

    while (true)
    {
        if (jackCount == 0 && jillCount == 0)
        {
            break;
        }


        for (int i = 0; i < jackCount; i++)
        {
            long value;
            std::cin >> value;
            jackVector.push_back(value);
        }

        long sharedCount = 0;
        for (int i = 0; i < jillCount; i++)
        {
            long value;
            std::cin >> value;
            
            for (int j = 0; j < jackVector.size(); j++)
            {
                if (value == jackVector[j])
                {
                    sharedCount++;
                }
            }

        }
    }

}
