from src import db, app
import os
import json

class DataManager:
    def save_user(self, user):
        if app.config['USE_DATABASE']:
            db.session.add(user)
            db.session.commit()
        else:
            file_path = f'persisitence/users/{user.username}.json'
            try: 
                if os.path.exists(file_path):
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                else:
                    data = []
            
                data.append(user.__dict__)

                with open(file_path, 'w') as file:
                    json.dump(data, file, indent=4)
            except Exception as e:
                print(f"Erreur lors de la sauvegarde de l'utilisateur dans un fichier: {e}")


    def save_amentity(self, amentity):
        if app.config['USE_DATABASE']:
            db.session.add(amentity)
            db.session.commit()
        else:
            file_path = f'persisitence/amentities/{amentity.name}.json'
            try: 
                if os.path.exists(file_path):
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                else:
                    data = []
            
                data.append(amentity.__dict__)

                with open(file_path, 'w') as file:
                    json.dump(data, file, indent=4)
            except Exception as e:
                print(f"Erreur lors de la sauvegarde de l'amenity dans un fichier: {e}")

    def save_base(self, base):
        if app.config['USE_DATABASE']:
            db.session.add(base)
            db.session.commit()
        else:
            file_path = f'persisitence/bases/{base.name}.json'
            try: 
                if os.path.exists(file_path):
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                else:
                    data = []
            
                data.append(base.__dict__)

                with open(file_path, 'w') as file:
                    json.dump(data, file, indent=4)
            except Exception as e:
                print(f"Erreur lors de la sauvegarde de la base dans un fichier: {e}")

        def save_city(self, city):
            if app.config['USE_DATABASE']:
                db.session.add(city)
                db.session.commit()
            else:
                file_path = f'persisitence/cities/{city.name}.json'
                try: 
                    if os.path.exists(file_path):
                        with open(file_path, 'r') as file:
                            data = json.load(file)
                    else:
                        data = []
                
                    data.append(city.__dict__)

                    with open(file_path, 'w') as file:
                        json.dump(data, file, indent=4)
                except Exception as e:
                    print(f"Erreur lors de la sauvegarde de la ville dans un fichier: {e}")

        def save_place(self, place):
            if app.config['USE_DATABASE']:
                db.session.add(place)
                db.session.commit()
            else:
                file_path = f'persisitence/places/{place.name}.json'
                try: 
                    if os.path.exists(file_path):
                        with open(file_path, 'r') as file:
                            data = json.load(file)
                    else:
                        data = []
                
                    data.append(place.__dict__)

                    with open(file_path, 'w') as file:
                        json.dump(data, file, indent=4)
                except Exception as e:
                    print(f"Erreur lors de la sauvegarde du lieu dans un fichier: {e}")

        def save_review(self, review):
            if app.config['USE_DATABASE']:
                db.session.add(review)
                db.session.commit()
            else:
                file_path = f'persisitence/reviews/{review.name}.json'
                try: 
                    if os.path.exists(file_path):
                        with open(file_path, 'r') as file:
                            data = json.load(file)
                    else:
                        data = []
                
                    data.append(review.__dict__)

                    with open(file_path, 'w') as file:
                        json.dump(data, file, indent=4)
                except Exception as e:
                    print(f"Erreur lors de la sauvegarde de la review dans un fichier: {e}")
