from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from validate_docbr import CPF, CNPJ
import uuid

# Create your models here.
class Profile(models.Model):
    DOC_TYPES = [
        ("CNPJ", "CNPJ"),
        ("CPF","CPF")
    ]

    account = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=255, default="")
    surname = models.CharField(max_length=255, default="", blank=True)
    doc = models.CharField(max_length=14, default="", unique=True)
    doc_type = models.CharField(choices=DOC_TYPES, max_length=4, default="")
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name
    
    def get_doc(self):
        if self.doc_type == "CNPJ":
            return {"type": "CNPJ", "doc": self.doc}
        elif self.doc_type == "CPF":
            return {"type": "CPF", "doc": self.doc}
        else: return {"type": "", "doc": ""}

    def get_fullname(self):
        return self.name + " " + self.surname
    
    def save(self, *args, **kwargs):
        if not self.account:
            raise ValidationError("O profile precisa estar atrelado a uma account")
        
        if not self.name:
            raise ValidationError("Nome de usuário obrigatório")
        
        if not self.doc:
            raise ValidationError("Documento é necessário para criar uma conta")
        
        if not self.doc_type:
            raise ValidationError("Documento é necessário para criar uma conta")

        if self.doc_type == "CNPJ":
            cnpj = CNPJ()
            validate = cnpj.validate(self.doc)
            if not validate:
                raise ValidationError("CNPJ Inválido")
        
        if self.doc_type == "CPF":
            cpf = CPF()
            validate = cpf.validate(self.doc)
            if not validate:
                raise ValidationError("CPF Inválido")

        super().save(*args, **kwargs)