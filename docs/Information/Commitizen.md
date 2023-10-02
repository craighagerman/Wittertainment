# On Commitizen

link: [https://github.com/commitizen-tools/commitizen]


## Quickstart on CLI commands

`cz bump` - bump version
`cz changelog` - generate changelog
`cz ch` - (same ^ )



## Use Commit Types

- `feat`: A new feature
- `fix`: A bug fix
- `chore`: Changes to build process or auxiliary tools
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests
- `breaking`: Breaking changes
- `revert`: Reverting to a previous commit


## Automated changelogs
see: [https://levelup.gitconnected.com/version-control-and-automatic-changelog-python-4d193ec90427]

Automatically update CHANGELOG.md by calling
```
cz bump --files-only
```


## Config
Commitizen config: [https://commitizen-tools.github.io/commitizen/config/]

Use .cz.toml config
```
  name = "cz_conventional_commits"
  tag_format = "$version"
  version_scheme = "semver"
  version = "0.0.1"
  update_changelog_on_bump = true
  major_version_zero = true
```

## On Conventional Commit
see: [https://www.conventionalcommits.org/]

## SemVer
see: [https://semver.org/]

- use Semantic Versioning 


## Other Useful Related Links

- (How To Automatically Generate A Helpful Changelog From Your Git Commit Messages)[https://mokkapps.de/blog/how-to-automatically-generate-a-helpful-changelog-from-your-git-commit-messages]


