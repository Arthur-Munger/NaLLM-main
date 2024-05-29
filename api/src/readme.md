components 总共9个文件，其中有6个文件与我们相关。
# 抽象类
1. base_component：被剩下的8个文件引用。

# Unstructured import
1. unstructed_data_extractor：主要划分为DataExtractor（不带Schema）和DataExtractorWithSchema
2. data_disambiguation: 这一部分主要是去除之前提取结果中重复的实体和关系。 
3. data_to_csv:将上面返回的结果转换为CSV文件，便于存储到本地，并将后面将提取的结果存储到图数据库中。

# Chat with KG
1. text2cypher：这个模块主要是将用户输入的问题转化为neo4j中的Cypher查询。
2. summarize_cypher_result：这一部分主要将上面转化的cypher查询以用户友好的方式转化给用户。
