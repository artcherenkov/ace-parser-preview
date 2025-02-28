<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <!-- Универсальная шаблонная копия для всех узлов -->
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <!-- Шаблон для элементов с переупорядочиванием атрибутов -->
    <xsl:template match="*">
        <xsl:copy>
            <!-- Вывод атрибута name, если есть -->
            <xsl:if test="@name">
                <xsl:attribute name="name">
                    <xsl:value-of select="@name"/>
                </xsl:attribute>
            </xsl:if>
            <!-- Вывод атрибута type, если есть -->
            <xsl:if test="@type">
                <xsl:attribute name="type">
                    <xsl:value-of select="@type"/>
                </xsl:attribute>
            </xsl:if>
            <!-- Вывод атрибута minOccurs, если есть -->
            <xsl:if test="@minOccurs">
                <xsl:attribute name="minOccurs">
                    <xsl:value-of select="@minOccurs"/>
                </xsl:attribute>
            </xsl:if>
            <!-- Вывод атрибута maxOccurs, если есть -->
            <xsl:if test="@maxOccurs">
                <xsl:attribute name="maxOccurs">
                    <xsl:value-of select="@maxOccurs"/>
                </xsl:attribute>
            </xsl:if>

            <!-- Вывод остальных атрибутов (например, отсортированных по имени) -->
            <xsl:for-each select="@*[not(local-name() = 'name' or local-name() = 'type' or local-name() = 'minOccurs' or local-name() = 'maxOccurs')]">
                <xsl:sort select="local-name()" data-type="text" order="ascending"/>
                <xsl:attribute name="{local-name()}">
                    <xsl:value-of select="."/>
                </xsl:attribute>
            </xsl:for-each>

            <!-- Обработка потомков -->
            <xsl:apply-templates select="node()"/>
        </xsl:copy>
    </xsl:template>

</xsl:stylesheet>
