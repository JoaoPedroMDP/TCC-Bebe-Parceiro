import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InspectGroupsComponent } from './inspect-groups.component';

describe('InspectGroupsComponent', () => {
  let component: InspectGroupsComponent;
  let fixture: ComponentFixture<InspectGroupsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InspectGroupsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InspectGroupsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
