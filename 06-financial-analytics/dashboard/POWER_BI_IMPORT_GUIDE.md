# Power BI Dashboard - Guia de Importação de Dados

## 📊 Arquivos Disponíveis para Importação

Todos os arquivos estão localizados em: `data/processed/`

### 1. **financial_metrics.csv** - Métricas Financeiras Principais
- **Uso**: Dashboard de Índices Financeiros
- **Período**: Q1 2022 - Q3 2025
- **Colunas principais**:
  - `period`: Período trimestral
  - `revenue`: Receita total
  - `profit_margin`, `roa`, `roe`: Indicadores de rentabilidade
  - `current_ratio`, `quick_ratio`: Índices de liquidez
  - `debt_to_equity`: Índice de alavancagem
  - `asset_turnover`: Giro de ativos

### 2. **revenue_forecast_data.csv** - Previsões de Receita
- **Uso**: Dashboard de Forecast e Projeções
- **Período**: Q4 2025 - Q4 2026
- **Colunas principais**:
  - `quarter`: Trimestre previsto
  - `moving_average_forecast`: Previsão por Média Móvel
  - `exponential_smoothing_forecast`: Previsão por Suavização Exponencial
  - `linear_regression_forecast`: Previsão por Regressão Linear
  - `consensus_forecast`: Previsão de Consenso (média dos 3 modelos)
  - `lower_confidence_bound`, `upper_confidence_bound`: Intervalo de confiança (95%)

### 3. **sales_performance.csv** - Performance de Vendas
- **Uso**: Dashboard de Vendas por Produto e Região
- **Período**: Jan 2024 - Out 2024 (Mensal)
- **Colunas principais**:
  - `month`, `year_month`: Período
  - `product_line`: Linha de Produto (A, B, C)
  - `region`: Região (North, South, East)
  - `units_sold`: Unidades vendidas
  - `revenue`: Receita
  - `gross_profit`, `gross_margin_percent`: Margem bruta

### 4. **profitability_analysis.csv** - Análise de Rentabilidade
- **Uso**: Dashboard de Lucratividade
- **Período**: Q1 2022 - Q3 2025 (Trimestral)
- **Colunas principais**:
  - `revenue`: Receita
  - `cogs`: Custo de Bens Vendidos
  - `gross_profit`: Lucro Bruto
  - `operating_income`: Lucro Operacional
  - `net_income`: Lucro Líquido
  - Múltiplos indicadores de margem percentual
  - `ebitda`, `ebitda_margin_percent`: EBITDA e margem

### 5. **regional_analysis.csv** - Análise Regional
- **Uso**: Dashboard de Desempenho Regional
- **Período**: Jan 2024 - Out 2024 (Mensal)
- **Colunas principais**:
  - `month`, `region`: Período e Região
  - `units_sold`, `revenue`: Vendas
  - `avg_price_per_unit`: Preço médio unitário
  - `market_share_percent`: Participação de mercado
  - `growth_rate_percent`: Taxa de crescimento

### 6. **market_indicators.csv** - Indicadores de Mercado
- **Uso**: Dashboard de Contexto de Mercado
- **Período**: Jan 2023 - Nov 2024 (Mensal)
- **Colunas principais**:
  - `market_index`: Índice de mercado
  - `interest_rate`: Taxa de juros
  - `inflation_rate`: Taxa de inflação
  - `consumer_confidence`: Confiança do consumidor
  - `market_sector_performance`: Performance do setor
  - `gdp_growth_percent`: Crescimento do PIB
  - `unemployment_rate`: Taxa de desemprego

### 7. **kpi_dashboard.csv** - Dashboard de KPIs
- **Uso**: Dashboard executivo com KPIs principais
- **Tipo**: Snapshot dos indicadores mais importantes
- **Colunas principais**:
  - `kpi_name`: Nome do indicador
  - `metric_type`: Tipo (Financial, Liquidity, Profitability, etc)
  - `current_value`: Valor atual
  - `target_value`: Valor alvo
  - `variance_percent`: Variação %
  - `trend`: Tendência (Upward/Downward/Stable)
  - `status`: Status (On Track, Good, Healthy, etc)

### 8. **balance_sheet.csv** - Balanço Patrimonial
- **Uso**: Dashboard Financeiro - Estrutura Patrimonial
- **Período**: Q1 2022 - Q3 2025 (Trimestral)
- **Colunas principais**:
  - `current_assets`, `fixed_assets`, `total_assets`: Ativos
  - `current_liabilities`, `long_term_debt`, `total_liabilities`: Passivos
  - `shareholders_equity`: Patrimônio Líquido
  - `retained_earnings`, `common_stock`: Componentes do PL

### 9. **income_statement.csv** - Demonstração de Resultados
- **Uso**: Dashboard de Resultados e Lucratividade
- **Período**: Q1 2022 - Q3 2025 (Trimestral)
- **Colunas principais**:
  - `revenue`: Receita total
  - `cost_of_goods_sold`: Custo de bens vendidos
  - `gross_profit`: Lucro bruto
  - `selling_general_admin`: SG&A
  - `operating_income`: Lucro operacional
  - `net_income`: Lucro líquido
  - `earnings_per_share`: Lucro por ação

---

## 🚀 Como Importar no Power BI

### Passo 1: Conectar aos dados
1. Abra **Power BI Desktop**
2. Clique em **Get Data** → **Text/CSV**
3. Navegue até a pasta `data/processed/`
4. Selecione o arquivo desejado

### Passo 2: Transformar os dados
1. Na janela de preview, clique em **Load** ou **Transform Data**
2. Se usar Transform Data (Power Query):
   - Verifique tipos de dados
   - Altere data/hora conforme necessário
   - Adicione colunas calculadas se necessário

### Passo 3: Criar Relacionamentos
Na aba **Model**:
- Crie relacionamentos entre tabelas usando:
  - `period`/`quarter`: Tabelas de tempo
  - `region`: Para análises regionais
  - `product_line`: Para análises de produto

### Passo 4: Criar Visualizações
Sugestões de gráficos:

**Dashboard 1 - Executivo**
- Card: Total Revenue (atual vs alvo)
- Card: Net Income (atual vs alvo)
- Linha: Trend de Revenue
- Gauge: Current Ratio (liquidez)
- Gauge: ROE (rentabilidade)

**Dashboard 2 - Vendas**
- Coluna: Revenue por Produto
- Mapa: Revenue por Região
- Tabela: Sales Performance detalhe
- Linha: Crescimento mensal

**Dashboard 3 - Forecast**
- Linha: Forecast vs histórico
- Área: Intervalo de confiança
- Tabela: Modelos de forecast comparação
- Card: Consenso 2026

**Dashboard 4 - Análise Financeira**
- Linha: Margens (Bruta, Operacional, Líquida)
- Linha: Índices financeiros (Liquidez, Alavancagem)
- Coluna: EBITDA vs Lucro Líquido
- Tabela: DRE detalhado

**Dashboard 5 - Mercado**
- Linha: Índice de mercado vs Revenue
- Linha: Confiança do consumidor vs Vendas
- Tabela: Indicadores macro

---

## 📝 Exemplo de DAX para Medidas Úteis

```dax
// Total Revenue
Total Revenue = SUM('financial_metrics'[revenue])

// Revenue Growth %
Revenue Growth % = 
    VAR Current = SUM('financial_metrics'[revenue])
    VAR Previous = CALCULATE(SUM('financial_metrics'[revenue]), 
        DATEADD('financial_metrics'[date], -1, QUARTER))
    RETURN (Current - Previous) / Previous * 100

// Average Profit Margin
Avg Profit Margin = AVERAGE('financial_metrics'[profit_margin])

// Target vs Actual
Variance % = 
    DIVIDE(
        SUM('kpi_dashboard'[current_value]) - SUM('kpi_dashboard'[target_value]),
        SUM('kpi_dashboard'[target_value])
    ) * 100
```

---

## 🔄 Atualizações de Dados

- **Financial Metrics**: Atualizar trimestralmente
- **Sales Performance**: Atualizar mensalmente
- **Market Indicators**: Atualizar mensalmente
- **Forecast Data**: Atualizar quando novos dados financeiros chegarem

---

## 📌 Notas Importantes

1. Todos os valores monetários estão em **USD**
2. Percentuais já estão no formato decimal (ex: 15.00 = 15%)
3. Datas estão no formato **YYYY-MM-DD** ISO
4. Use **Locale PT-BR** para formatação de números se necessário
5. Considere adicionar um **Slicer de Data** para facilitar análises temporais

---

*Documento criado em: Novembro 2025*
