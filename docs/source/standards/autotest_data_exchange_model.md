# AutoTest数据交换模型

规范英文名：AutoTest Data Exchange Model

规范中文名：AutoTest数据交换模型

**标识名：autotest_data_exchange_model**

**版本：v1.0.0**



## 总体说明

本文档用于定义AutoTest的各类数据与外部交换的标准模型，包括案例模板（Case Template）、测试数据（Test Data）、测试案例（Test Case）、测试集（Test Set）等，与其他框架的输入和输出均采用该数据模型。

本文档中的所有模型均为标准XML格式，要求XML的所有标签均无属性（便于转换为JSON），根标签统一为autotest，固定有一个meta标签，登记模型的基本信息：

- type ： 模型类型
- ver ： 模型版本号

示例如下：

```
<?xml version="1.0" encoding="utf-8"?>
<autotest>
  <!-- 基本信息 -->
  <meta>
    <type>CaseTemplate</type>
    <ver>1.0.0</ver>
  </meta>
  <!-- 具体模型信息 -->
  ...
</autotest>
```



## 动态值处理

对于所有模型中的值类型的标签，均可以使用动态值处理插件在生成执行案例时进行值的处理，规范是在值域填值的时候，以"**{$plugin_id=**要处理的值字符串**$}**"来定义要处理的动态值，可以支持多层嵌套，或多个处理。

例如：

```
<para>取值为{$python=1+1$}，{$javascript='结果为'+{$python=2+2$}$}</para>
动态计算后结果为
<para>取值为2，结果为4</para>
```



## 案例模板（Case Template）

案例模板（Case Template）用于定义测试案例（Test Case）的默认信息，如果不与测试数据组合，可以直接通过案例模板直接生成测试案例（只不过案例的数据采用的是默认值）；当案例模板与测试数据结合在一起，可以按照测试数据的个数生成相应数量的测试案例。

案例模板的总体模型如下：

```
<?xml version="1.0" encoding="utf-8"?>
<autotest>
  <!-- 基本信息 -->
  <meta>
    <type>CaseTemplate</type>
    <ver>1.0.0</ver>
  </meta>
  <!-- 具体模型信息 -->
  <case_info>
  	<!-- 案例信息 -->
  </case_info>
  <premise_job>
    <!-- 前置任务信息 -->
  </premise_job>
  <test_data>
    <!-- 测试数据信息 -->
  </test_data>
  <check>
    <!-- 测试结果检查信息 -->
  </check>
  <execute_plugin_para>
    <!-- 执行插件运行参数 -->
  </execute_plugin_para>
</autotest>
```



### 案例信息（case_info）

记录测试案例的具体信息，相关信息不会参与测试任务的执行，只是用于登记，类似于手工执行的案例的案例信息管理。

**必须的标签：**

- domain : 测试区域，用于区分不同案例归属不同区域，同时可以通过domain区分不同的机构，例如ms.windows可以代表微软公司的windows区域

- template_no : 模板编号，可自定义或由系统生成，该编号在一个domain中必须唯一

- manager_type_id : 管理分类ID，用于将案例分类进行管理

- case_name : 案例名称

- desc : 案例说明

- version : 案例版本，从1.0.0开始，每次修改进行变更

- author : 作者（编写人）

- create_time : 创建时间，格式为"yyyy-mm-dd hh24:mi:ss"

- execute_plugin_id : 案例执行插件ID

  

**非必须的标签：**

- type : 案例类型，枚举类型（normal - 正向案例，reverse - 反向案例）

- premise : 前提条件，案例执行的前提说明

- step : 测试步骤，案例执行的步骤说明

- test_data : 数据要求，案例执行的测试数据说明

- check : 检查方案，测试后验证测试是否通过的检查说明

- last_edit_user : 最后修改人

- last_eidt_time : 最后修改时间，格式为"yyyy-mm-dd hh24:mi:ss"

- change_log : 案例修改日志，该信息包含4个子标签

  - change_user : 修改人
  - change_time : 修改时间
  - version : 修改后的版本
  - change_desc : 修改说明

  

### 前置任务信息（premise_job）

登记执行当前案例前需要先执行的工作任务，包括需要先执行的测试案例（依赖），或者一些公共数据的准备（把数据查到内存供后续访问），或者执行一些操作（如数据库更新、执行操作系统命令等）。

可放置多个前置任务，每个任务的主标签是任务ID，需注意的是前置任务将按顺序执行。

示例如下：

```
  <premise_job>
    <!-- 前置任务信息 -->
    <job_id_1>
    	<name>任务名</name>
    	<plugin_id>任务插件ID</plugin_id>
    	<para1>执行参数1</para1>
    	<para2>执行参数2</para2>
    </job_id_1>
    <job_id_2>
      ...
    </job_id_2>
    ...
  </premise_job>
```



**必须的标签：**

- name : 任务名

- plugin_id : 任务插件ID，可以通过扩展插件的方式增加支持；内置的插件只有PremiseTestCase，执行依赖的测试案例

  

**插件运行参数标签：**

根据插件的不同，对应的运行参数标签不同，例如对于PremiseTestCase，参数标签为：

- domain : 测试案例对应的测试区域
- case_no : 测试案例编号



### 测试数据信息（test_data）

登记案例测试执行所需的数据，或生成数据对应的动态脚本。在模板中的数据设置不会区分数据用途（例如是子报文数据、报文头数据还是报文体数据），需具体案例执行插件自行根据数据参数判断和处理。

可放置多个测试数据项，每个测试数据项的主标签是数据ID，需注意的是数据项动态更新会按顺序执行，因此在动态脚本中引用其他数据项时要注意这个限制。

示例如下：

```
  <test_data>
    <!-- 测试数据信息 -->
    <data_id_1>
      <en_name>英文名</en_name>
      <cn_name>中文名</cn_name>
      <value>数据取值</value>
      <para1>案例执行插件参数</para1>
      <para2>案例执行插件参数</para2>
    </data_id_1>
    <data_id_2>
      ...
    </data_id_2>
    ...
  </test_data>
```

**必须的标签：**

- en_name : 数据英文名
- cn_name : 数据中文名
- value : 数据取值

**插件运行参数标签：**

根据案例执行插件的不同，对应的运行参数标签不同。



### 测试结果检查信息（check）

登记测试案例执行后，检查测试结果是否通过的验证条件。可以设置多个检查条件，只有所有检查条件都通过的情况下，测试才算成功。

可放置多个结果检查项，每个检查项的主标签是检查ID。

示例如下：

```
  <check>
    <!-- 测试结果检查信息 -->
    <check_id_1>
      <desc>检查说明</desc>
      <plugin_id>检查插件ID</plugin_id>
      <para1>检查插件运行参数</para1>
      <para2>检查插件运行参数</para2>
    </check_id_1>
    <check_id_2>
      ...
    </check_id_2>
    ...
  </check>
```

**必须的标签：**

- desc : 检查说明
- plugin_id : 检查插件ID

**插件运行参数标签：**

根据检查插件的不同，对应的运行参数标签不同。



### 执行插件运行参数（execute_plugin_para）

针对执行插件所设置的参数，根据不同的插件对应的参数有所不同，具体见执行插件对应的说明材料。



## 测试数据（Test Data）

测试数据（Test Data）用于定义生成测试案例的测试数据，可以在一个测试数据配置文件中设定多个测试案例的数据。

测试数据的总体模型如下：

```
<?xml version="1.0" encoding="utf-8"?>
<autotest>
  <!-- 基本信息 -->
  <meta>
    <type>TestData</type>
    <ver>1.0.0</ver>
  </meta>
  <data_info>
    <!-- 数据基本信息 -->
  </data_info>
  <data_list>
    <!-- 测试数据列表 -->
    <case>
      <!-- 案例数据 -->
      <case_info>
  	    <!-- 案例信息 -->
      </case_info>
      <premise_job>
        <!-- 前置任务信息 -->
      </premise_job>
      <test_data>
        <!-- 测试数据信息 -->
      </test_data>
      <check>
        <!-- 测试结果检查信息 -->
      </check>
    </case>
    <case>
      ...
    </case>
    ...
  </data_list>
</autotest>
```



### 数据基本信息（data_info）

记录测试数据的具体信息，相关信息不会参与测试任务的执行，只是用于登记。

**必须的标签：**

- template_no : 测试数据对应的模板编号
- desc : 测试数据总体说明

- version : 数据版本，从1.0.0开始，每次修改进行变更
- author : 作者（编写人）
- create_time : 创建时间，格式为"yyyy-mm-dd hh24:mi:ss"

**非必须的标签：**

- last_edit_user : 最后修改人

- last_eidt_time : 最后修改时间，格式为"yyyy-mm-dd hh24:mi:ss"

- change_log :  修改日志，该信息包含4个子标签

  - change_user : 修改人
  - change_time : 修改时间
  - version : 修改后的版本
  - change_desc : 修改说明

  

### 测试数据列表（data_list）

存放多个测试案例数据的列表，每一个<case>标签包含一个测试案例对应的数据，数据的组织形式与测试模板相同，包括案例信息（case_info）、前置任务信息（premise_job）、测试数据信息（test_data）、测试结果检查信息（check）四个标签。

四个标签里的内容，如果与对应测试模板中的关键字（例如任务名）一致，则代表覆盖测试模板中的相应内容；如果设置测试模板中不存在的内容，则代表在测试模板的基础上增加相应内容（放置到最后）；如果没有设置对应的标签或内容，则代表沿用测试模板的内容。

**案例信息（case_info）**

新增的标签：

- case_no : 案例编号，对应数据生成的案例编号


不会继承的标签：

- template_no : 模板编号，可自定义或由系统生成，该编号在一个domain中必须唯一


- author : 作者（编写人）
- create_time : 创建时间，格式为"yyyy-mm-dd hh24:mi:ss"
- execute_plugin_id : 案例执行插件ID
- last_edit_user : 最后修改人
- last_eidt_time : 最后修改时间，格式为"yyyy-mm-dd hh24:mi:ss"
- change_log : 案例修改日志，该信息包含4个子标签

**前置任务信息（premise_job）**

对应测试模板的内容关键字为<job_id_1>标签名

**测试数据信息（test_data）**

对应测试模板的内容关键字为<data_id_1>标签名

**测试结果检查信息**（check）

对应测试模板的内容关键字为<check_id_1>标签名



## 测试集（Test Set）

多个案例模板或测试案例数据的集合，用于将需要一并执行的案例模板或测试数据放置在一起，便于快速生成测试任务。



## 测试案例（Test Case）

测试案例是在生成测试任务的时候，同步根据案例模板及测试数据生成，用于在测试任务中执行。测试案例的模型与案例模板一致，只是在案例信息（case_info）中增加了case_no 标签。