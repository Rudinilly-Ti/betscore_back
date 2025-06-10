from .partidas_crud import get_partidas  # Certifique-se de que está importando o correto
from .partidas_ao_vivo import partidas_ao_vivo  # Certifique-se de que outras views estão incluídas
from .partidas_agendadas import get_agenda
from .agenda_time import get_agenda_time  # Importa a view para agendar partidas de um time
from .classificacao import get_classificacao  # Importa a view para obter os times