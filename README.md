## Valence

Valence returns following results:
- only negative
- mostly negative
- mostly neutral
- mostly positive
- only positive
- only neutral
- mostly mixed
- only mixed

## Sample proccessing

Service takes input:
```
{
  "messages": [
    {
      "content": "See on p\u00e4ris huvitav asi, mida anal\u00fc\u00fcsida. Korpus v\u00f5iks veidi parem ja suurem olla siiski.."
    }
  ]
}
```

Modifies it:
```
{
  "messages": [
    {
      "content": "See on p\u00e4ris huvitav asi, mida anal\u00fc\u00fcsida. Korpus v\u00f5iks veidi parem ja suurem olla siiski..",
      "valence": "only positive"
    }
  ]
}
```

And writes it to output. If given input has invalid structure then given file will be ignored

## Running locally

Run `docker-compose -f docker-compose-valence.yml up`. Provide input like it is visible in the file system.

## When developing

- change valence-analyzer to valence in `docker-compose-valence.yml`
- Comment out line 3 in `Dockerfile-valence`
- Run `docker-compose -f docker-compose-build-valence.yml up --build`
- Comment in line 13 in `docker-compose-valence.yml`
- Run `docker-compose -f docker-compose-valence.yml up --build`
