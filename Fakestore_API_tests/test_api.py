import requests


def test_get_user():
    response = requests.get('https://fakestoreapi.com/carts/5')
    assert response.status_code == 200
    assert response.json()['id'] == 5
    assert response.json()['userId'] == 3


def test_assert_data_all_carts():
    response = requests.get('https://fakestoreapi.com/carts')
    assert response.status_code == 200
    carts = response.json()
    for cart in carts:
        assert cart["id"]
        assert cart["userId"]
        assert cart["date"]
        assert cart["products"]

def test_add_new_product():
    #Automated as per docs; product POST isn't actually inserted so expected data is approximate and uses seeded data
    post = requests.post('https://fakestoreapi.com/carts',json=
                        {
                            'id': '5',
                            'date': '2020-02-03',
                            'products': '[{productId:7,quantity:1},{productId:8,quantity:1}]'
                        })
    assert post.status_code == 200
    response = requests.get('https://fakestoreapi.com/carts/5')
    cart = response.json()
    assert cart['products'] == [{'productId': 7, 'quantity': 1}, {'productId': 8, 'quantity': 1}]
    
def test_update_new_product():
    #Automated as per docs; product PATCH isn't actually inserted so expected data is approximate and uses seeded data
    patch = requests.patch('https://fakestoreapi.com/carts/5',json=
                        {
                            'date': '2020-02-03',
                            'products': '[{productId:7,quantity:3}]'
                        })
    assert patch.status_code == 200
    #response = requests.get('https://fakestoreapi.com/carts/5')
    #cart = response.json()
    #assert cart['products'] == [{'productId': 7, 'quantity': 3}, {'productId': 8, 'quantity': 1}]

def test_delete_cart():
    #Automated as per docs; product PATCH isn't actually inserted so expected data is approximate and uses seeded data
    delete = requests.delete('https://fakestoreapi.com/carts/5')
    assert delete.status_code == 200
    #deletion doesn't occur; deletion check commented out 
    #response = requests.get('https://fakestoreapi.com/carts/5')
    #cart = response.json()
    #assert cart['products'] == [...]
    