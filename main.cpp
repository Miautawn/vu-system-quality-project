#include <iostream>
#include <vector>

using namespace std;

class rs_m
{
public:
    vector<double> r; 

    void setResort(vector<double> r)
    {
        this->r = r;
    }

    //getting the size of the resort
    double GetResortSize() 
    {
        int len = r.size();
        return len;
    }

    int show()
    {
        for (int i = 0; i < r.size(); i++)
        {
            cout << r[i] << " ";
        }
        cout << endl;
    }
};

class RSMclient
{
public:
    vector<string> c;

    //setting clients
    void setClient(vector<string> c)
    {
        this->c = c;
    }

    int GetClientCount(int k) 
    {
        int len = c.size();
        return len;
    }

    void printClientDetails()
    {
        for (int i = 0; i < c.size(); i++)
        {
                    cout << c[i] << " ";}
                    cout << endl;
    }
};

class RestaurantMenu
{
private:
    std::vector<std::string> menuItems; 

public:
    void setMenuItems(const std::vector<std::string>& items)
    {
        menuItems = items;
    }
};

int main()
{
    //initializing the resort and the rooms
    rs_m res;
    vector<double> data = {101, 102, 103}; 

    res.setResort(data);
    double size = res.GetResortSize(); 
    cout << "Size of the resort: " << size << endl;
    res.show();

    //initializing the clients
    RSMclient client;
    vector<string> clientData = {"John", "Alice", "Bob"}; 

    client.setClient(clientData);
    int clientCount = client.GetClientCount(2);
    cout << "Number of clients: " << clientCount << endl;
    client.printClientDetails();

    return 0;
}
