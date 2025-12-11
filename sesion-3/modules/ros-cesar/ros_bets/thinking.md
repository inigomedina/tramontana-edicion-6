### caso de uso simple (no entramos en multiples ni otros mercados) ### 

Entidades principales: 
- Usuario 
- Evento
- Markets (tipos de apuestas a resultados) 
- Bets 

## Por qué necesitamos markets como tabla fuera ## 
Cada evento tiene distintos tipos de apuestas. Lo más conocido es el 1x2 (home vs. away) pero hay un sinfín de resultados: a números de goles, quién marca, asistencias... y tipos de apuestas predetermiandas: a medio timepo etc. 
Por simplicidad, en el ejercicio uso estos markets pero dejo el tipo de apuesta a simple (una única selección por apuesta)

## relación entre entidades ## 
Un mismo usuario puede tener varias bets. 
Un evento tiene muchas opciones de apuesta (markets/cuotas)
Un market pertenece a un solo evento, pero puede ser utilizado por más de un usuario 

## diseño simple ## 
Users
* id, name, email, balance, created_at
Events
* id, name, home_team, away_team, sport, competition, event_date, status, result, created_at
Markets
* id, event_id, market_type, selection, odds, created_at
Bets
* id, user_id, market_id, stake_amount, potential_winnings, status, actual_winnings, placed_at, settled_at


___ 

┌─────────┐
│  Users  │
│  id     │───┐
│  name   │   │
│  balance│   │ 1:N
└─────────┘   │
              │
              ↓
         ┌─────────┐
         │  Bets   │
         │  id     │
         │  user_id│ (FK)
    ┌────│market_id│ (FK)
    │    │  stake  │
    │    └─────────┘
    │         ↑
    │         │ N:1
    │         │
    │    ┌─────────┐
    │    │ Markets │
    │    │  id     │
    └────│event_id │ (FK)
         │selection│
         │  odds   │
         └─────────┘
              ↑
              │ N:1
              │
         ┌─────────┐
         │ Events  │
         │  id     │
         │  name   │
         │ result  │
         └─────────┘

