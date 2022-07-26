# Copyright 2022 99Cloud, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel, Field


# Shared properties
class RSUQueryResultDataBase(BaseModel):
    result_id: int = Field(..., description="Result ID")
    data: Dict[str, Any] = Field(..., description="Result Data")


# Properties to receive via API on creation
class RSUQueryResultDataCreate(RSUQueryResultDataBase):
    """"""


class RSUQueryResultDataInDBBase(RSUQueryResultDataBase):
    id: int = Field(..., alias="id", description="RSU Query Result Data ID")

    class Config:
        orm_mode = True


# Additional properties to return via API
class RSUQueryResultData(RSUQueryResultDataInDBBase):
    """"""


class RSUQueryResultDatas(BaseModel):
    """"""
