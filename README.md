# 数据处理公共 project
## 1、SUMO 关键命令
（1）转换 OSM 数据：`netconvert --osm-files your_map.osm -o your_map.net.xml --geometry.remove`

（2）生成交通需求：`python $SUMO_HOME/tools/randomTrips.py -n your_map.net.xml -o your_trips.rou.xml -e 3600 --validate`  

（3）验证路线：`duarouter --net-file your_map.net.xml --route-files your_trips.rou.xml --output-file validated_routes.rou.xml`  

（4）配置仿真文件（your_simulation.sumocfg）：
``
<configuration>
    <input>
        <net-file value="your_map.net.xml"/>
        <route-files value="validated_routes.rou.xml"/>
    </input>
    <time>
        <begin value="0"/>
        <end value="3600"/>
    </time>
    <output>
        <fcd-output value="your_trajectory.xml"/>
        <tripinfo-output value="tripinfo.xml"/>
    </output>
</configuration>
``  
（5）运行仿真：`sumo -c your_simulation.sumocfg`  

