# Integração NBS X AutoDeal

### Ambiente
- [x] Criar arquivo .env
## Extract 

### Dados NBS
- [x] Criar Conexão com Banco de dados intermediário NBS-AutoDeal
- [ ] Criar Schemas com base nas consultas para criação
- [ ] Criar Schemas com base nas consultas para alteração

## Load
### API AWS - AutoDeal / URL: https://autodeal.organizaprime.com.br/login 
- [x] Obter Token com API 
- [x] Mapear MetadataKeys
- [ ] Criar Novo Processo (Concluido parcialmente)
- [ ] Alterar Processo


### Estrutura prevista
``` bash
autodeal_sync/
├── domain/
│   └── models.py
├── infra/
│   └── database.py
├── services/
│   ├── sender.py
│   ├── retry.py
│   └── reconciliation.py
├── api_client/
│   └── autodeal.py
├── repositories/
├── jobs/
│   └── sync_job.py