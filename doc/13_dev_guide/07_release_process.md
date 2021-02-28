# Pashmak Release Process
We have 3 type of release like every project: micro release, minor release, major release.

We have sperated branches for minor releases. for example, if `0.7` is released, we should create a branch named `0.7` for that. then, we can release micro releases inside that branch(`0.7.1`, `0.7.5`, `0.7.15`...).

- The Micro releases are for bug fixes.(`0.0.x`)
- The Minor releases are for new features. Its better to be backward compatible but can accept small backward incompatible changes. (`0.x.x`)
- The Major release is for big releases and may have backward hard incompatible changes(`x.x.x`)

### Pre releases
We have `alpha`, `beta` and `rc` pre releases. pre releases are only for minor and major releases(not for micro releases).

for example `1.0-alpha1`, `0.7-beta5`, `0.9-rc6`... are pre releases.

### Branches
Branching is so easy. We have seprated branches in minor and major releases. for example, `0.7` or `1.0`.

When we make some changes in `0.7` branch(example), we should merge this to forward branches.

for example, we have 3 releases(still supported):

- `0.7`
- `0.8`
- `1.0`
- `master`

When we fix a bug in `0.7`, we should merge `0.7 to -> 0.8`. then merge `0.8 to -> 1.0` and `0.1 to -> master`. In this process, we should fix conflicts.

Also we should handle `CHANGELOG.md` file.

The `master` branch is the next minor/major release.

## Making a release
To make a release, we should do the following steps:

1. Make a branch:

```bash
git checkout -b release-x.y.z
# OR if you are using git-flow
git flow release start vx.y.z <base>
```

2. Bump the version number:

There is a script in `scripts/release.pashm` for bumping version number:

```bash
python3 src/pashmak.py scripts/release.pashm x.y.z
```

(Replace `x.y.z` with the new version number).

3. Update the change log:

The `scripts/release.pashm` script replaces automatically `## next release` string to `## x.y.x (YYYY-MM-DD)`, But maybe you should edit it manually

4. Commit the changes:

```bash
git add -A
git commit -m 'x.y.z'
```

6. Run the tests and scripts:

```bash
make all
# ON Windows
.\win-configure.bat
```

6. Merge the branch

```bash
git checkout master && git merge release-x.y.z && git tag vx.y.z
# OR if you are using git-flow
git flow release finish x.y.z
```

7. Finish

Now, new release is ready, push the changes and tags:

```bash
git push --follow-tags
```

Now, you can see the new version:

```bash
./src/pashmak.py -v
```

