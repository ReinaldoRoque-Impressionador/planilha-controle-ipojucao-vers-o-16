# database.py

#from flask_sqlalchemy import SQLAlchemy

# Criando instância global que será usada em toda a aplicação
# database = SQLAlchemy()

# modulos/banco/database.py

from sqlalchemy import text

from sqlalchemy import inspect, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import text

#from modulos.banco import db_models  # Isso garante que todas as classes estejam registradas

def inserir_usuarios_desenvolvedores():
    from modulos.banco.db_models import Usuario
    db = SessionLocal()

    usuarios_dev = [
        Usuario(nome="Raphael", email="cebous@hotmail.com.br", senha="1234", perfil="dev"),
        Usuario(nome="Reinaldo", email="roquereinaldo@gmail.com", senha="975624asa", perfil="dev")
    ]

    for usuario in usuarios_dev:
        existente = db.query(Usuario).filter_by(email=usuario.email).first()
        if not existente:
            db.add(usuario)

    db.commit()
    db.close()


def usar_sessao():
    from banco.database import SessionLocal  # importação local evita ciclo
    session = SessionLocal()

# Caminho do banco — você pode mudar para uma pasta específica se quiser
DATABASE_URL = "sqlite:///./modulos/banco/meubanco.db"

# Criação do engine e da sessão
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

database = SessionLocal()


# Base para os modelos
Base = declarative_base()

session = SessionLocal()

def inicializar_banco():
    print("🔄 Criando tabelas...")
    from modulos.banco import db_models  # ✅ Importa os modelos depois que Base existe

    Base.metadata.create_all(bind=engine)
    print("✅ Banco pronto!")


# def inicializar_banco():
#     from sqlalchemy import inspect
#     inspector = inspect(engine)
#     if not inspector.has_table("usuarios"):  # ou qualquer tabela-chave
#         print("🔄 Criando tabelas...")
#         Base.metadata.create_all(bind=engine)
#         print("✅ Banco pronto!")
#     else:
#         print("⚠️ Tabelas já existem. Nenhuma ação necessária.")

def inicializar_banco():
    print("🔄 Verificando e criando tabelas...")
    Base.metadata.create_all(bind=engine)
    print("✅ Banco pronto!")

def testar_conexao():
    from sqlalchemy import inspect, text
    from sqlalchemy.exc import SQLAlchemyError
    from modulos.banco.db_models import Cliente, Pagamento

    try:
        db = SessionLocal()

        # 1. Teste básico com expressão textual correta
        resultado = db.execute(text("SELECT 1"))
        print("✅ Conexão básica OK:", resultado.fetchone())

        # 2. Verificar tabelas existentes
        inspetor = inspect(db.bind)
        tabelas = inspetor.get_table_names()
        print("📋 Tabelas encontradas:", tabelas)

        # 3. Verificar se há dados nas tabelas principais
        cliente_count = db.query(Cliente).count()
        pagamento_count = db.query(Pagamento).count()

        print(f"👤 Clientes cadastrados: {cliente_count}")
        print(f"💳 Pagamentos registrados: {pagamento_count}")

    except SQLAlchemyError as e:
        print("❌ Erro ao conectar ou consultar o banco:")
        print(e)
    finally:
        db.close()
# def testar_conexao():
#     from sqlalchemy.exc import SQLAlchemyError
#
#     try:
#         db = SessionLocal()
#         resultado = db.execute("SELECT 1")
#         print("✅ Conexão com o banco de dados bem-sucedida!")
#         print("Resultado:", resultado.fetchone())
#     except SQLAlchemyError as e:
#         print("❌ Erro ao conectar com o banco de dados:")
#         print(e)
#     finally:
#         db.close()