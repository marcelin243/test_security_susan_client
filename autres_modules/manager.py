from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(("L'email ne peut pas etre vide"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
      

    # def create_superuser(self, email, password=None, **extra_fields):
    #     """
    #     Pour la création de super utilisateur
    #     """
    #     # Assurer que les attributs pour super utilisateur sont bien définis
    #     extra_fields.setdefault('telephone', "6531449")
    #     # extra_fields.setdefault('acteur_id', "1")

    #     # if extra_fields.get('is_staff') is not True:
    #     #     raise ValueError('Le super utilisateur doit avoir is_staff=True.')
    #     # if extra_fields.get('is_superuser') is not True:
    #     #     raise ValueError('Le super utilisateur doit avoir is_superuser=True.')

    #     return self.create_user(email, password, **extra_fields)