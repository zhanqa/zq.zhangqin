---

---

# GIT的原理及基本使用

## 一、什么是GIT

 GIT，全称是分布式管理控制系统，是一款分布式源代码管理工具，git通常在编程中会用到，并且git支持分布式部署，可以有效、高速的处理从很小到非常大的项目版本管理。分布式相比于集中式的最大区别在于开发者可以提交到本地，每个开发者通过克隆（git clone），在本地机器上拷贝一个完整的Git仓库。

## 二、GIT的简单了解

### 1.git分为那几个区？分别是什么？

①工作区(Workspace)是电脑中实际的目录。

②暂存区(Index)类似于缓存区域，临时保存你的改动。

③仓库区(Repository)，分为本地仓库和远程仓库。

### 2.git 与 svn的区别？

svn 集中式代码版本控制管理工具

git 分布式代码版本控制管理工具 git 最流行

svn集中式的如果出现svn服务器出现故障每个用户都不能访问服务器代码无法同步 ，git就没有这种问题

### 3.git与github、码云、gitlab的关系

github、码云、gitlab都是在线的代码托管平台，他们都支持git管理代码的方式 

github.com: 全球最大免费代码托管平台 

码云: 国内免费代码托管平台 

gitlab:企业项目开发使用广泛

## 三、GIT的基本原理

### 1. Git采用的是全量存储方案

​	所谓全量方案，就是每个版本都保存所有的数据（多是代码，文件占据空间较小）。优点：快速；缺点：浪费空间。

​	与此相对的是增量方案：保存的是上一个版本 + 补丁。优点：节省空间；缺点：要进行运算，费时。

### 2. 文件变动信息的存储

​	git把每次文件的改动都存在项目根目录下的.git文件夹中。

### 3. .git文件夹中的文件

- 利用哈希算法SHA-1计算得到文件的哈希值，依据此哈希值来判断文件内容是否有改变。

  **注：由于哈希值是唯一的（几乎不会重复），所以可以保证同一个文件只存储一份。**

- 使用 `tree` 结构来存储

  文件是叶节点，文件夹是非叶节点

### 4. 暂存区

通常在很多传统集中式版本控制系统中，只有两个空间用来管理你的数据，一个是你的working copy（工作区），另一个便是 datastore（版本库），然而在Git中，引入了staging area（index）这一概念，我们可以把它看做一个“码头”，你来决定其中的哪些改变可以被“运走”。有了暂存区，我们的工作区边和Git库就不再直接挂钩了，这样我们可以更加灵活的控制我们的数据了，对暂存区的操作非常的简单，git add可以将你工作区的文件添加到暂存区中，git commit 可以将暂存区中的文件提交到版本库中。

### 5. 快照链表

​	`HEAD` 指针指向最新的快照。

​	想恢复某个版本，就把指针指向那个版本，然后使用 `checkout` 命令；或者直接 `checkout` 那个版本的哈希值。

### 6. 协同和分支

​	项目需要多人分别开发时（假设两人开发），可以在 `master` 主分支进行 `checkout` 操作，分出两个分支，每个人在自己的分支进行开发工作，开发完成后进行合并操作。有两种合并方式：

- `merge`：合并时，两个分支和这两个分支的公共祖先进行三方合并。

- `rebase`：将A分支保存到一个临时目录下，然后撤销此分支上所有commit，再将B分支的commit接到这条分支上（此时两个分支基本一致），最后再将临时目录下保存的内容接到这条分支后。若此时删掉B分支，则此时就只有一条包含所有功能的分支

  **注：rebase会修改提交记录*

## 四、GIT的使用

### （一）GIT的基本命令

#### 1. 本地库初始化

在项目的根目录进行操作：

```bash
git init
```

#注意：生成的 .git 目录中存放的是本地库相关文件，不要删除

#### 2. 设置签名

签名的作用是区分不同操者身份。用户信息在每一个版本提交中能够看到，以此确认本次提交是谁做的。

（1）项目(仓库)级别`仅在当前本地库有效`

```bash
1.git config user.name tom # 设置用户名

2.tomgit config user.email du@qq.com # 设置用户邮箱
```

（2）系统用户级别`仅在当前登录的操作系统用户有效`

```bash
1.git config --global user.name tom

2.git config --global user.email du@qq.com
```

> 注：仅仅加了一个 `--global`
>
> **优先级别：`项目级别`  >  `系统级别`**
>
> **信息保存位置：`~/.gitconfig 文件`，即C盘下的用户目录**

#### 3. 添加文件（到暂存区）

```bash
1.git add fileName  # 指定文件
2.git add . # 所有
3.# 将工作区的文件添加到暂存区
```

#### 4. 查看状态

```bash
git status   # 查看工作区、暂存区状态
```

#### 5. 提交（到本地库）

```bash
git commit -m 'commit message'
```

将暂存区内容提交到本地库

#### 6. 创建分支

```bash
git branch dev_dxx
```

创建名称为dev_dxx的分支

#### 7. 切换分支

```bash
git checkout dev_dxx
```

切换到dev_dxx分支

#### 8. 查看分支

```bash
git branch -v
```

#### 9. 合并分支

```bash
1.git branch dev_aaa

2.git checkout dev_aaa # 新建一个分支并切换过来# ...  对文件进行更改  # 合并分支的时候要明确谁谁合并

3.git checkout master # 回到master分支进行merge

4.git merge dev_dxx # 先合并dev_dxx，不会有冲突，因为此分支相当于是对master进行后续操作

5.git merge dev_aaa # 再合并dev_aaa，若修改过同一个文件，则此时会有冲突conflict
```

#### 10. 解决merge冲突

（1）放弃合并

```bash
git merge --abort
```

（2）手动合并冲突

打开有冲突的文件，文件内有冲突的部分会以下述形式分隔开来

```markdown
1.<<<<<<<<<<<<<< 

2.当前分支的代码

3.============== 

4.合并过来的代码

5.>>>>>>>>>>>>>>
```

（3）重新添加并提交

```sql
1.git add fileName

2.git commit -m 'merged' 
```

#### 11. 查看日志

```bash
1.git log # 查看所有的版本记录

2.git reflog # 可以查看所有分支的所有操作记录（包括已经被删除的 commit 记录和 reset 的操作）
```

### （二）Git结合Github

#### 1. 创建远程仓库

在 Github 上新建远程仓库

#### 2. 添加远程版本库

```bash
git remote add 别名 远程地址 
```

#### 3.查看远程地址别名

```bash
git remote -v
```

#### 4. 推送 push

```bash
1.git push 别名 分支名

2.git push -u 别名 分支名    # -u指定默认主机
```

#### 5. 克隆 clone

将远程仓库的项目克隆到本地，clone进行一次从无到有的过程，更新用 pull

```bash
git clone 远程地址
```

####  6. 拉取 pull

本地已经存在 clone 下来的文件，用 pull 进行更新

```bash
1.# pull = fetch + merge

2.git fetch 别名 分支名

3.git merge 别名 分支名

4.# 等价于

5.git pull 别名 分支名
```

#### 7. 删除git与github的联系

```bash
git remote remove origin # origin是本仓库在github上的别名
```

#### 8. fork

用于团队外协作，其他人员使用 fork 将代码拉到自己的远程仓库中，可以直接进行更改，也可以 pull 到本地更改后 push 到远程仓库，之后进行 pull request，等待原有团队审核后 merge 即可。











